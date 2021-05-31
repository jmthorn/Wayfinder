from app.models import db, Default_destination

# Adds a demo user, you can add other users here if you want
def seed_default_destinations():

    D1 = Default_destination(
        name='Mount Bonnell', 
        city_id=1,
        description="Mount Bonnell, also known as Covert Park, is a prominent point alongside the Lake Austin portion of the Colorado River in Austin, Texas. It has been a popular tourist destination since the 1850s.The mount provides a vista for viewing the city of Austin, Lake Austin, and the surrounding hills. It was designated a Recorded Texas Historic Landmark in 1969, bearing Marker number 6473, and was listed on the National Register of Historic Places in 2015.",
        image_url="https://s3.amazonaws.com/crowdriff-media/full/674a9801ccfd6801489c79c0abaa6aad42a65e4e2b3c87ffb24d14513e457f0d.jpg",
        address="Mt Bonnell, Austin, TX 78731",
        lat=30.321982413719372,
        long= -97.77325451940332,
        duration="30"
        )
    D2 = Default_destination(
        name='Texas State Capitol', 
        city_id=1,
        description="If it's in Texas, it must be bigger and better. That is the motto that architects followed with the Capitol Building in Austin. At one time, it was the tallest capitol building in the nation. Others might be taller now, but this is still a beautiful building that shows off many of the natural resources which are so prevalent in Texas, such as limestone and the landscapes.",
        image_url="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/04/16/1f/48/state-capitol.jpg?w=2000&h=-1&s=1",
        address="1100 S Congress Ave, Austin, TX 78704-1728",
        lat= 30.253491428576755,
        long= -97.74795390244505,
        duration="180"
        )
    D3 = Default_destination(
        name='Lady Bird Lake Hike-and-Bike Trail', 
        city_id=1,
        description="In the heart of Austin is the Ann and Roy Butler Hike-and-Bike Trail at Lady Bird Lake, a lush, urban path that meanders along the water’s edge and passes by skyscrapers, neighborhoods, ball fields and cultural attractions. With the completion of the Boardwalk portion of the Trail in June 2014, the 1.3 mile gap along the south shore has been closed, and the Trail now serves our city in an additional way – as an alternative transportation route for our growing urban core.",
        image_url="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/dc/2f/93/skyline-from-auditorium.jpg?w=1000&h=-1&s=1",
        address="Ann and Roy Butler Hike and Bike Trail, Austin, TX",
        lat=30.25924009716859,
        long= -97.74361154477457,
        duration="120"
        )
    D4 = Default_destination(
        name='Barton Springs Pool', 
        city_id=1,
        description="Barton Springs Pool is a recreational outdoor swimming pool that is filled entirely with water from nearby natural springs. It is located on the grounds of Zilker Park in Austin, Texas. The pool exists within the channel of Barton Creek and utilizes water from Main Barton Spring, the fourth largest spring in Texas.",
        image_url="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/a7/ed/83/barton-springs-pool-in.jpg?w=2000&h=-1&s=1",
        address="2201 Barton Springs Rd Zilker Park, Austin, TX 78746-5736",
        lat=30.263847899088887,
        long= -97.77072147984568,
        duration="120"
        )
    D5 = Default_destination(
        name='Blanton Museum of Art', 
        city_id=1,
        description="The Jack S. Blanton Museum of Art at the University of Texas at Austin is one of the largest university art museums in the U.S. with 189,340 square feet devoted to temporary exhibitions, permanent collection galleries, storage, administrative offices, classrooms, a print study room, an auditorium, shop, and cafe.",
        image_url="https://tiltedchair.co/wp-content/uploads/2018/03/blanton-1.jpg",
        address="200 E Martin Luther King Jr Blvd, Austin, TX 78712",
        lat=30.281176617091877,
        long= -97.73748063127977,
        duration="120"
        )
    D6 = Default_destination(
        name='Franklin Barbecue', 
        city_id=1,
        description="A standout star within Austin’s heavyweight barbecue scene, Franklin draws lines that are as epic as its world-renowned brisket. Take a tip from the regulars: come early, come hungry, and come with a collapsible chair (you don't want to stand for three or four hours if you can avoid it). Just don’t miss that luscious oak-smoked brisket with its distinctive peppery exterior; it’s tender enough to cut with a spoon. ",
        image_url="https://3q87le1gsko01ibim33e4wib-wpengine.netdna-ssl.com/wp-content/uploads/2019/06/FranklinBBQ-plate-1024x576.jpg",
        address="900 E 11th St, Austin, TX 78702",
        lat=30.270310836585907,
        long= -97.73119834292794,
        duration="120"
        )
    D7 = Default_destination(
        name='Laguna Gloria', 
        city_id=1,
        description="The Contemporary Austin - Laguna Gloria, formerly known as the AMOA-Arthouse at Laguna Gloria, is the former home of Clara Driscoll and site of a 1916 Italianate-style villa on the shores of Lake Austin in Austin, Texas. It was the original home of the Austin Museum of Art and still houses some of its collections.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cc/AMOA-Laguna_Gloria.jpg",
        address="3809 W 35th St, Austin, TX 78703",
        lat=30.31225638878753,
        long= -97.77432200244392,
        duration="90"
        )
    D8 = Default_destination(
        name='"I Love You So Much" Mural', 
        city_id=1,
        description="Located on buzzing South Congress Avenue, on one side of the popular Jo's Coffee, it's a green painted wall bearing a simple message in elegant red text: \"I love you so much\". You don't need tickets, but you will almost certainly need to wait your turn in line for a few minutes to have a photograph taken (that's where Jo's Coffee comes in handy - try the signature TURBO: a sweet, chocolatey iced coffee that Austinites swear by).",
        image_url="https://media.cntraveler.com/photos/602eb315a6d0560b658128a0/16:9/w_2560%2Cc_limit/CWXCP6.jpg",
        address="1300 S. Congress Ave.",
        lat=30.249568237770504,
        long= -97.74940244477476,
        duration="30"
        )
    D9 = Default_destination(
        name='Zilker Botanical Garden', 
        city_id=1,
        description="The Zilker Botanical Garden is a botanical garden of varied topography located on the south bank of the Colorado River at 2220 Barton Springs Road, near downtown Austin, Texas, United States. The Botanical Garden was established as a non-profit organization in 1955, and is the centerpiece of Zilker Park.",
        image_url="https://www.austintexas.gov/sites/default/files/files/ZBG/zbg_2.jpg",
        address="2220 Barton Springs Rd, Austin, TX 78746",
        lat=30.268976634592487,
        long= -97.77147873127997,
        duration="150"
        )
    D10 = Default_destination(
        name='Central Machine Works', 
        city_id=1,
        description="Central Machine Works is a big, airy beer hall and microbrewery in east Austin. It has a light, bright warehouse vibe (it's a converted machine works, hence the name). Picture one big, expansive space with high ceilings, enormous windows and deep leather sofas to sink into as you sample their pleasantly extensive beer menu.",
        image_url="https://media.cntraveler.com/photos/602eb3868fa4fc6a56a7c39f/16:9/w_2560%2Cc_limit/Andrea_Calo_19671.jpg",
        address="4824 E Cesar Chavez St, Austin, TX 78702",
        lat=30.252124427103283,
        long= -97.70158853128031,
        duration="120"
        )

    D11 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D12 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D13 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D14 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D15 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D16 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D17 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D18 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D19 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D20 = Default_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D21 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D22 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D23 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D24 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D25 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D26 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D27 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D28 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D29 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D30 = Default_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D31 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D32 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D33 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D34 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D35 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D36 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D37 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D38 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D39 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D40 = Default_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D41 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D42 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D43 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D44 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D45 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D46 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D47 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D48 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D49 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )
    D50 = Default_destination(
        name='', 
        city_id=5,
        description="",
        image_url="",
        address="",
        lat=,
        long= ,
        duration=""
        )



    db.session.add(D1)
    db.session.add(D2)
    db.session.add(D3)
    db.session.add(D4)
    db.session.add(D5)
    db.session.add(D6)
    db.session.add(D7)
    db.session.add(D8)
    db.session.add(D9)
    db.session.add(D10)
    db.session.add(D11)
    db.session.add(D12)
    db.session.add(D13)
    db.session.add(D14)
    db.session.add(D15)
    db.session.add(D16)
    db.session.add(D17)
    db.session.add(D18)
    db.session.add(D19)
    db.session.add(D20)
    db.session.add(D21)
    db.session.add(D22)
    db.session.add(D23)
    db.session.add(D24)
    db.session.add(D25)
    db.session.add(D26)
    db.session.add(D27)
    db.session.add(D28)
    db.session.add(D29)
    db.session.add(D30)
    db.session.add(D31)
    db.session.add(D32)
    db.session.add(D33)
    db.session.add(D34)
    db.session.add(D35)
    db.session.add(D36)
    db.session.add(D37)
    db.session.add(D38)
    db.session.add(D39)
    db.session.add(D40)
    db.session.add(D41)
    db.session.add(D42)
    db.session.add(D43)
    db.session.add(D44)
    db.session.add(D45)
    db.session.add(D46)
    db.session.add(D47)
    db.session.add(D48)
    db.session.add(D49)
    db.session.add(D50)


    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_default_destinations():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()