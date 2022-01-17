import pytest
from app import app
from utils import parse
from models.Item import Item
from models.Receipt import Receipt


@pytest.fixture
def t_client():
    return app.test_client()


class TestApi:
    def test_post_input1(self, t_client):
        input_data = ("2 book at 12.49" + "\n"
                      "1 music CD at 14.99" + "\n"
                      "1 chocolate bar at 0.85")
        headers = {
            'Content-Type': 'text/plain'
        }
        response = t_client.post(
            '/api/v1/receipts',
            headers=headers,
            data=input_data
        )
        assert response.status_code == 200
        assert response.data.decode() == ("2 book: 24.98" + "\n"
                                          "1 music CD: 16.49" + "\n"
                                          "1 chocolate bar: 0.85" + "\n"
                                          "Sales Taxes: 1.50" + "\n"
                                          "Total: 42.32")

    def test_post_input2(self, t_client):
        input_data = ("1 imported box of chocolates at 10.00" + "\n"
                      "1 imported bottle of perfume at 47.50")
        headers = {
            'Content-Type': 'text/plain'
        }
        response = t_client.post(
            '/api/v1/receipts', headers=headers, data=input_data)

        assert response.status_code == 200

        assert response.data.decode() == ("1 imported box of chocolates: 10.50" + "\n"
                                          "1 imported bottle of perfume: 54.65" + "\n"
                                          "Sales Taxes: 7.65" + "\n"
                                          "Total: 65.15")

    def test_post_input3(self, t_client):
        input_data = ("1 imported bottle of perfume at 27.99" + "\n"
                      "1 bottle of perfume at 18.99" + "\n"
                      "1 packet of headache pills at 9.75" + "\n"
                      "3 box of imported chocolates at 11.25")
        headers = {
            'Content-Type': 'text/plain'
        }
        response = t_client.post(
            '/api/v1/receipts', headers=headers, data=input_data)

        assert response.status_code == 200

        assert response.data.decode() == ("1 imported bottle of perfume: 32.19" + "\n"
                                          "1 bottle of perfume: 20.89" + "\n"
                                          "1 packet of headache pills: 9.75" + "\n"
                                          "3 imported box of chocolates: 35.55" + "\n"
                                          "Sales Taxes: 7.90" + "\n"
                                          "Total: 98.38")


class TestItem:
    def test_exempt_item(self):
        item = Item("book", 1, 10, False)
        assert item.taxes() == 0
        assert item.total() == 10
        assert item.isExempt() == True
        assert item.toString() == "1 book: 10.00"

    def test_not_exempt_item(self):
        item = Item("music CD", 1, 12, False)
        assert item.taxes() == 1.2
        assert item.total() == 13.2
        assert item.isExempt() == False
        assert item.toString() == "1 music CD: 13.20"

    def test_imported_exempt_item(self):
        item = Item("imported book", 2, 10, True)
        assert item.taxes() == 1
        assert item.total() == 21
        assert item.isExempt() == True
        assert item.toString() == "2 imported book: 21.00"

    def test_imported_not_exempt_item(self):
        item = Item("imported music CD", 1, 10, True)
        assert item.taxes() == 1.5
        assert item.total() == 11.5
        assert item.isExempt() == False


class TestReceipt:
    def test_receipt_no_item(self):
        items = []
        receipt = Receipt(items)
        assert len(receipt.items) == 0
        assert receipt.taxes() == 0
        assert receipt.total() == 0
        assert receipt.toString() == ("No Items" + "\n"
                                      "Sales Taxes: 0.00"+"\n"
                                      "Total: 0.00"
                                      )

    def test_receipt_exempt(self):
        items = [
            Item("book", 1, 10, False),
            Item("chocolate", 1, 10, False),
            Item("pills", 1, 10, False),
        ]
        receipt = Receipt(items)
        assert len(receipt.items) == 3
        assert receipt.taxes() == 0
        assert receipt.total() == 30
        assert receipt.toString() == ("1 book: 10.00"+"\n"
                                      "1 chocolate: 10.00"+"\n"
                                      "1 pills: 10.00"+"\n"
                                      "Sales Taxes: 0.00"+"\n"
                                      "Total: 30.00"
                                      )

    def test_receipt_imported_exempt(self):
        items = [
            Item("imported book", 1, 10, True),
            Item("imported chocolate", 1, 10, True),
            Item("imported pills", 1, 10, True),
        ]
        receipt = Receipt(items)
        assert len(receipt.items) == 3
        assert receipt.taxes() == 1.5
        assert receipt.total() == 31.5
        assert receipt.toString() == ("1 imported book: 10.50"+"\n"
                                      "1 imported chocolate: 10.50"+"\n"
                                      "1 imported pills: 10.50"+"\n"
                                      "Sales Taxes: 1.50"+"\n"
                                      "Total: 31.50"
                                      )

    def test_receipt_imported_not_exempt(self):
        items = [
            Item("imported music CD", 1, 10, True),
            Item("imported parfume", 1, 10, True),
            Item("imported phone", 1, 10, True),
        ]
        receipt = Receipt(items)
        assert len(receipt.items) == 3
        assert receipt.taxes() == 4.5
        assert receipt.total() == 34.5
        assert receipt.toString() == ("1 imported music CD: 11.50"+"\n"
                                      "1 imported parfume: 11.50"+"\n"
                                      "1 imported phone: 11.50"+"\n"
                                      "Sales Taxes: 4.50"+"\n"
                                      "Total: 34.50"
                                      )


class TestUtils:
    def test_parse_ok(self):
        input_data = ("1 imported music CD at 32.15" + "\n"
                      "2 bottle of perfume at 18.99")
        items = parse(input_data)
        assert len(items) == 2

        assert items[0].name == "imported music CD"
        assert items[0].qty == 1
        assert items[0].price == 32.15
        assert items[0].imported == True

        assert items[1].name == "bottle of perfume"
        assert items[1].qty == 2
        assert items[1].price == 18.99
        assert items[1].imported == False

    def test_parse_ko(self):
        input_data = ("wrong input")
        items = parse(input_data)
        assert len(items) == 0
