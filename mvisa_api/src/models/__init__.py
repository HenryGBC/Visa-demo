# coding: utf-8

"""
    mVisa API

    mVisa is a simple, secure and fast way to pay and be paid using mobile phones. mVisa enables a range of payment use cases and is technology agnostic-leveraging evolving POS environment such as QR codes and works on both smart or feature phones.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .address import Address
from .card_acceptor import CardAcceptor
from .cash_in_push_payments_getget_response import CashInPushPaymentsGetgetResponse
from .cash_in_push_paymentspost_payload import CashInPushPaymentspostPayload
from .cash_in_push_paymentspost_response import CashInPushPaymentspostResponse
from .cash_out_payments_getget_response import CashOutPaymentsGetgetResponse
from .cash_out_push_payments_postpost_payload import CashOutPushPaymentsPostpostPayload
from .cash_out_push_payments_postpost_response import CashOutPushPaymentsPostpostResponse
from .merchant_push_payment_getget_response import MerchantPushPaymentGetgetResponse
from .merchant_push_payments_postpost_payload import MerchantPushPaymentsPostpostPayload
from .merchant_push_payments_postpost_response import MerchantPushPaymentsPostpostResponse
from .purchase_identifier import PurchaseIdentifier

# ----------------------------------------------------------------------------------------------------------------------
# © Copyright 2018 Visa. All Rights Reserved.
#
# NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
# and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
# rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.
#
# By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy
# (developer.visa.com/privacy). In addition, all permissible uses of the Software must be in support of Visa products,
# programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com).
# THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL
# FAULTS” BASIS WITHOUT WARRANTY OR CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.
# ----------------------------------------------------------------------------------------------------------------------