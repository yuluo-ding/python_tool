# /user/bin/python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

xml_doc="""
    <?xml version='1.0' encoding='UTF-8'?>
<SPY_CONFIG BUILD="20141120&amp;YJMIX2014093001" VERSION="3.0">
	<HTTPSPY>
		<SITE ID="100" DOMAIN="WEIWEIWNAG" NAME="WEIWEIWNAG" TYPE="HTTPSHOP" DESCRIPTION="ceshi" >
			<!-- login -->
			<FILTER METHOD="POST" URL="/userLogin.jhtml" HOST="mobile.homevv.com" MSG_TYPE="SHOPPING_LOGIN" />
			<!-- addaddress -->
			<FILTER METHOD="POST" URL="/appAddUserAddress.jhtml" HOST="mobile.homevv.com" MSG_TYPE="SHOPPING_ADDR_VIEW" />
			<!-- addresslist -->
			<FILTER METHOD="POST" URL="/appUserAddress.jhtml" HOST="mobile.homevv.com" MSG_TYPE="SHOPPING_ADDR_VIEW" />
			<!-- android order -->
			<FILTER METHOD="POST" URL="/appSubmitOrder.jhtml" HOST="mobile.homevv.com" MSG_TYPE="SHOPPING_ORDER" />
			<!-- android detail -->
			<FILTER METHOD="POST" URL="/viewOrder.jhtml" HOST="mobile.homevv.com" MSG_TYPE="SHOPPING_ORDER" />
			<!-- android orderlist -->
			<FILTER METHOD="POST" URL="/searchOrderList.jhtml" HOST="mobile.homevv.com" MSG_TYPE="SHOPPING_ORDERLIST_VIEW" />

		</SITE>
	</HTTPSPY>
</SPY_CONFIG>

"""

soup = BeautifulSoup(xml_doc)

# print soup.prettify()
print soup.SITE
# print soup.SITE['DESCRIPTION']