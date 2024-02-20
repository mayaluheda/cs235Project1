from page_objects.PageTiktok import PageTiktok
import time

def test_like_control():
    # login with your active tiktok account
    scenario_num = 28 #change this number here for different scenarios!
    username = "Sec02Gr1Sc28Activ_SH" #replace JL with your initial
    page = PageTiktok(scenario_num,username)
    page.fetch_tiktok()
    time.sleep(60)
    page.iterate_through_batches_like_control()
    time.sleep(10)


