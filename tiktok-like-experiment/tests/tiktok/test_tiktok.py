from page_objects.PageTiktok import PageTiktok
import time

class TiktokAudit(PageTiktok):
    def control_run(self):
        self.fetch_tiktok()
        self.iterate_through_batches()
        time.sleep(10)
"""
    def test_like_random(self):
        self.fetch_tiktok()
        self.iterate_through_batches_like_random()
        time.sleep(10)
        self.chromebrowser.close()
"""

