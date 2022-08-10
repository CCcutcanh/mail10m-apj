import pymailtm
p = pymailtm.MailTm()
password = p._generate_password(8)
domain = str(p._get_domains_list()[0])
create = p._make_account_request("accounts",p._generate_password(6).lower() + '@' + domain, password)
print(create)
address = create["address"]
_id = create["id"]
print(address)
x = pymailtm.Account(_id, address, password)
print(x.get_messages())
print(x.wait_for_message())
