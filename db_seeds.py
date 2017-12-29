#!/usr/bin/env python3
'''
Created on Dec 15, 2017

@author: messiry
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Cat_Item, Base, Category, User

engine = create_engine('sqlite:///Catalogue.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Creating Dummy Users 

User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

User2 = User(name="mohammed monir", email="monir@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

User3 = User(name="mohammed khalil", email="khalil@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User3)
session.commit()

User4 = User(name="dummy dummy", email="dummy@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User4)
session.commit()

User5 = User(name="hala mohammed", email="halamohammed@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User5)
session.commit()

User6 = User(name="sarah el emshaty", email="sarahelemshaty@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User6)
session.commit()

# Create dummy categories with dummy items

category = Category(name='SnowBoarding', user_id=1,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis." )
session.add(category)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User1,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Helmet',category=category, user = User1,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Goggles',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='SnowBoard',category=category, user = User6,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()


#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#

category = Category(name='Basketball',user_id=1,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(category)
session.commit()

Item = Cat_Item(name='Jersey',category=category, user = User1,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()
Item = Cat_Item(name='Shorts',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Basket Balls',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Rest Bands',category=category, user = User1,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#


category = Category(name='Football',user_id=2,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(category)
session.commit()

Item = Cat_Item(name='Jersey',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Shorts',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Foot Ball',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Knee Pads',category=category, user = User4,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#

category = Category(name='Skating',user_id=3 ,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(category)
session.commit()


Item = Cat_Item(name='Skate Board',category=category, user = User3,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Arm Pads',category=category, user = User3,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Knee Pads',category=category, user = User3,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Helmet',category=category, user = User3,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()


#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#


category = Category(name='Hockey',user_id=4,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(category)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User4,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User4,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User4,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User4,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()


#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#


category = Category(name='Swimming',user_id=5,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(category)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User3,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Stick',category=category, user = User3,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#


category = Category(name='Weight Lifting',user_id=6,
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(category)
session.commit()

Item = Cat_Item(name='Dumbles',category=category, user = User6,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Ez Bar',category=category, user = User6,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Weight Gloves',category=category, user = User6,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='Back support Belt',category=category, user = User5,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='knee protection',category=category, user = User2,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

Item = Cat_Item(name='sweat band',category=category, user = User4,
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada dictum nisi, ac tincidunt arcu. Nullam fringilla lectus ac accumsan pretium. Aenean id ex at leo faucibus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla euismod massa eu tellus posuere porta. Vivamus interdum vel urna ut iaculis. Vivamus tempor mattis mi in lacinia. Pellentesque sodales arcu mi, a vulputate tortor porttitor eu. Cras faucibus eros pharetra, vestibulum neque sed, condimentum purus. Phasellus consectetur risus ac gravida sagittis.")
session.add(Item)
session.commit()

#-----------------------------------------------------#
#-----------------------------------------------------#
#-----------------------------------------------------#

print(" Database Seeds Planted successfully !!")