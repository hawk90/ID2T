import Test.ID2TAttackTest as Test
import ID2TLib.TestLibrary as Lib

sha_default = 'a45bd543ae7416cdc5fd76c886f48990b43075753931683407686aac2cfbc111'
sha_ips_not_in_pcap = 'bb3926cea75624124777422b68de8f1e699b3219e279f5a9bcd789ed837aa349'
sha_multiple_params = '6a39bafde84f30c63389c35ba24446d5aabb8e8942ee3a34974556211d6091d8'

# TODO: improve coverage


class UnitTestJoomla(Test.ID2TAttackTest):

    def test_joomla_default(self):
        self.checksum_test([['JoomlaRegPrivExploit']], sha_default)

    def test_joomla_ips_not_in_pcap(self):
        self.checksum_test([['JoomlaRegPrivExploit', 'ip.src=1.1.1.1', 'ip.dst=2.2.2.2']], sha_ips_not_in_pcap)

    def test_joomla_multiple_params(self):
        ip_src = 'ip.src='+Lib.test_pcap_ips[0]
        ip_dst = 'ip.dst='+Lib.test_pcap_ips[1]
        self.checksum_test([['JoomlaRegPrivExploit', ip_src, ip_dst, 'mac.src=00:0C:21:1C:60:61',
                             'mac.dst=04:0C:32:2C:63:62', 'port.dst=42',
                             'target.host=www.ihopethisisnotarealwebsite.com']], sha_multiple_params)
