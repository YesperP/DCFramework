import json
from PersonClient import Person, PaymentDto


def print_response(response):
    print(json.dumps(response.json(), indent=4, sort_keys=False))


def main():
    # Make person object with SSN
    p = Person(29105573083)

    account_print = False
    card_print = True
    customer_print = True
    payment_print = True


    # ACCOUNTS:
    if account_print:
        accounts = p.get_accounts()
        print_response(accounts)

        account_number = accounts.json()['accounts'][0]['accountNumber']

        account_details = p.get_account_details(account_number)
        print_response(account_details)

        account_balance = p.get_account_balance(account_number)
        print_response(account_balance)

    # CARDS:
    if card_print:
        cards = p.get_cards()
        print_response(cards)

        card_id = cards.json()[1]['cardId']

        print_response(p.get_card_details(card_id))

        # PS: Only works for credit cards. Use get_account_balance for debit cards.
        print_response(p.get_card_balance(card_id))

        # Card in pos 0 has flag unblockAllowed=true
        print_response(p.put_unblock_card(cards.json()[0]['cardId']))

    # CUSTOMERS
    if customer_print:
        print_response(p.get_customer_details())

    # PAYMENT - Static data still so why did I even do this?
    if payment_print:
        accounts = p.get_accounts()

        debit = accounts.json()['accounts'][0]['accountNumber']
        credit = accounts.json()['accounts'][1]['accountNumber']

        payDto = PaymentDto(None, debit, credit, 200, "2019-03-09", None, None, None)

        # Getting 403 here, maybe I am not so good.
        print(p.post_initiate_payment(json.dumps(payDto.__dict__)))

        print_response(p.get_transactions(debit))

if __name__ == "__main__":
    main()