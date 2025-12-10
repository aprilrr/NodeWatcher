# test_nodewatcher.py
"""
Tests for NodeWatcher module.
"""

import unittest
from nodewatcher import NodeWatcher

class TestNodeWatcher(unittest.TestCase):
    """Test cases for NodeWatcher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeWatcher()
        self.assertIsInstance(instance, NodeWatcher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeWatcher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
