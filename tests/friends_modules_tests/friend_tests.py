import unittest

from Class.friends_modules.friend import Friend

class TestFriendClass(unittest.TestCase):

    def test_parse_selection_input(self):
        mock_selection = {'text': '', 'image': '', 'values': [4, 'Meshtastic eec8', '!7a6beec8', 'eec8', 'TBEAM', '40.0369°', '-75.4965°', '101%', 'None', '0.10%', 'None', '0/unknown', 'None', 'None'], 'open': 0, 'tags': ''}
        
        new_friend = Friend().parse_selection_input(mock_selection)
        
        print(new_friend.__dict__)
        self.assertEqual(
            "Meshtastic eec8",
            new_friend.username
        )
        
        expected_values = {'radio_id': '', 'n': 4, 'username': 'Meshtastic eec8', 'id': '!7a6beec8', 'aka': 'eec8', 'hardware': 'TBEAM', 'latitude': '40.0369°', 'longitude': '-75.4965°', 'battery': '101%', 'channel util.': 'None', 'tx air util.': '0.10%', 'snr': 'None', 'hops away': '0/unknown', 'lastheard': 'None', 'since': 'None'}
        for k, v in expected_values.items():
            self.assertEqual(
                expected_values[k],
                new_friend.__getattribute__(k)
            )
        
if __name__ == '__main__':
    unittest.main()