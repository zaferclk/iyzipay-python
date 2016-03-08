import pprint
import unittest
import iyzipay


class BinNumberSample(unittest.TestCase):
    def runTest(self):
        self.should_retrieve_bin_number()

    def should_retrieve_bin_number(self):

        options = {'base_url': iyzipay.base_url}
        options.update({'api_key': iyzipay.api_key})
        options.update({'secret_key': iyzipay.secret_key})

        request = {'locale': 'TR'}
        request.update({'conversationId': '123456'})
        request.update({'binNumber': '454671'})

        bin_number = iyzipay.BinNumber.retrieve(request, options)

        pprint.pprint(bin_number.read().decode())