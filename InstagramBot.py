from instapy import InstaPy 
session = InstaPy (username = "your Username", password = "your password")
session.login()

session.set_relationship_bounds(enabled = True, max_followers =200 )

session.set_do_like(enabled=True, percentage=40)
#ignore any keywords that may be offensive to comment under such as Rest in peace or 
#Not safe for work
session.set_ignore_if_contains(['RIP', 'R.I.P', 'angel', 'NSFW'])

session.like_by_tags(amount=10, use_smart_hashtags=True)

session.set_skip_users(skip_private=True,
                       skip_no_profile_pic=True,
                       skip_business=True,
                       skip_business_categories=['Creators & Celebrities'])
