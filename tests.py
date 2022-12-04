import unittest

class TestDNSResolver(unittest.TestCase):
  def test_dns_query(self):
    resolver = DNSResolver()

    query = b'\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x07google\x03com\x00\x00\x01\x00\x01'

    result = resolver.dns_query(query)

    self.assertEqual(result, b'\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x07google\x03com\x00\x00\x01\x00\x01')

if __name__ == '__main__':
  unittest.main()
