from app.models import db, Custom_destination

# Adds a demo user, you can add other users here if you want
def seed_custom_destinations():

    D1 = Custom_destination(
        name='Torchy\'s Tacos', 
        city_id=1,
        description="An Austin original serving specialty tacos made with a passion. Torchy’s customers, employees, friends and fans share in the Taco Dream. Prepare to be addicted! Several Austin area locations.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d1.jpeg",
        address="1822 S Congress Ave, Austin, TX 78704",
        lat=30.245621744100376,
        lng= -97.75158020244523,
        duration=60,
        user_id=1
        )
    D2 = Custom_destination(
        name='Slurpin\' Ramen Bar', 
        city_id=2,
        description="Started in the heart of Koreatown, Los Angeles 8th Street, Slurpin ramen was created from ambition to bringing authentic Hakata-style  rich, thick and creamy tonkotsu ramen to California. Slurpin’ derives from Japanese culture in showing respect to your ramen chef with a loud “slurp” sound from eating the noodles and broth.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d2.jpeg",
        address="3500 W 8th St, Los Angeles, CA 90005",
        lat=34.07001707893153,
        lng= -118.30809265784463,
        duration=60,
        user_id=1
        )
    D3 = Custom_destination(
        name='Gas Works Park', 
        city_id=3,
        description="Gas Works Park is a park located in Seattle, Washington, United States. It is a 19.1-acre public park on the site of the former Seattle Gas Light Company gasification plant, located on the north shore of Lake Union at the south end of the Wallingford neighborhood.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d3.jpg",
        address="2101 N Northlake Way, Seattle, WA 98103",
        lat=47.64630557402461,
        lng= -122.33368897320506,
        duration=120,
        user_id=1
        )
    D4 = Custom_destination(
        name='Toufuya Ukai', 
        city_id=5,
        description="The restaurant features beautiful pine trees and a pond where Koi carp swim. Passing in front of the garden lantern and waterwheel and walking on the steppingstones, you will find yourself back in time in the town of Edo, the Tokyo of 200 years ago. Please enjoy the extraordinary atmosphere in the restaurant with 6,600 m² of extensive Japanese gardens located at the foot of Tokyo Tower.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d4.jpeg",
        address="4 Chome-4-13 Shibakoen, Minato City, Tokyo 105-0011, Japan",
        lat=37.70220703131334,
        lng= 139.89131454959846,
        duration=80,
        user_id=1
        )
    D5 = Custom_destination(
        name='Ling-Ling\'s Bali', 
        city_id=4,
        description="Located in the heart of Seminyak, Ling Ling's offers contemporary asian fusion basing our core ideals on Japanese & Korean styles. We strive for our customers satisfaction with our endless supply of asian tapas to our most delectable drinks menu. Open from 12pm everyday to satisfy your hunger for an exquisite meal, a heavenly refreshment, tunes for the soul or just a fun night out with friends.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d5.jpeg",
        address="Jl. Petitenget no. 43B, Seminyak 80361 Indonesia",
        lat=-8.673867098817842,
        lng= 115.15738463949066,
        duration=80,
        user_id=1
        )
    D6 = Custom_destination(
        name='Diamond Jubilee Tea Salon at Fortnum & Mason', 
        city_id=6,
        description="This historic spot for afternoon tea has been an upper crust British favorite since it began importing leaves from Asia in 1707. It's no wonder the beloved tearoom was reopened in 2012 by the Queen after a sensitive refit. The room retains a fittingly regal affect, decorated in the store’s trademark eau de nil (take that, Tiffany). There’s often a pianist tinkling away in the corner of the airy elegant room in the afternoon. The tea itself will leave even the most discerning of tea snobs with their mouths open. There are 50 different blends and tea sommeliers to help you chose which one is for you.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/61.jpeg",
        address="4th Floor, Fortnum & Mason, 181 Piccadilly, St. James's, London W1A 1ER, United Kingdom",
        lat= 55.74684553651231,
        lng= 0.5625023010493078,
        duration=80,
        user_id=1
        )
    D7 = Custom_destination(
        name='Company\'s Garden', 
        city_id=7,
        description="This historic site was at the heart of the first European settlement in Cape Town: The colony was set up to serve as a refreshment station for ships passing the tip of Africa to head to the east, and the Company's Garden was started as a farm to grow produce for them. Now it's a peaceful oasis in the middle of the Central Business District, with a series of beautifully manicured gardens and green areas where you'll find children chasing squirrels, office workers on lunch break, and any number of performers.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/7.11.jpeg",
        address="15 Queen Victoria St, Cape Town City Centre, Cape Town, 8001, South Africa",
        lat= -31.080244907759603,
        lng= 18.55564223006794,
        duration=120,
        user_id=1
        )
    D8 = Custom_destination(
        name='South Bank', 
        city_id=6,
        description="The South Bank is one of the London’s best bits. Generally located between the Westminster and London bridges, it offers about two-miles of excellent, largely state-funded arts and entertainment venues alongside breezy, traffic-free views of a succession of city landmarks (Big Ben, St. Paul's, the Tower of London) that lie on the north bank. No wonder it attracts over 14 million people per year. If you have limited time in the capital, South Bank is great because it has everything, including a selection of good restaurants and street food offerings.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c8.jpeg",
        address="South Bank, London, UK",
        lat= 51.5043071920616,
        lng= -0.11176605183219414,
        duration=120,
        user_id=1
        )
    D9= Custom_destination(
        name='Tate Modern', 
        city_id=6,
        description="This former oil-fired power station sits smugly in the center of the South Bank, knowing that you’re interested in what’s going on inside. It’s filled to the rafters with paintings and sculptures by the likes of Picasso, Dali, Warhol, and Rothko, all set off perfectly by that gritty industrial interior. The collections span 1500 to the present day but are split into abstract themes rather than eras—don’t think too hard, just pick one and dive in. And it’s rare that any exhibition at Tate Modern is awaited with anything less than bated breath. Whether they’re the paid shows across the mid-levels of the institution or the vast and clever commissions to take over the massive space that is the Turbine Hall, you’re pretty much bound to be blown away. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c9.jpeg",
        address="Tate Modern, London, UK",
        lat= 51.507841178543984,
        lng= -0.09922628837008483,
        duration=120,
        user_id=1
        )
    D10 = Custom_destination(
        name='London\'s Lidos', 
        city_id=6,
        description="There’s something very British about clinging to the open-air life even when it’s wet and cold. London’s lidos (pronounced lee-doze) embody this attitude. Dating from the 1920s and ’30s, these outdoor cold-water pools substitute for seaside resorts on sunny days, and serve the needs of fitness nuts on wintry ones. But mostly they make for a perfect outing, complete with cafés, hot showers, and plenty of kids’ facilities. Four of the best, dotted around London’s extraordinary parks, are at Brockwell, Charlton, Parliament Hill, and London Fields. There’s no more exhilarating feeling than your circulation pumping as you pry yourself out of the water. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c10.jpeg",
        address="London Fields West Side London, E8 3EU United Kingdom",
        lat= 51.54193384317877,
        lng= -0.06180200186133957,
        duration=120,
        user_id=1
        )
    D11 = Custom_destination(
        name='King\'s Cross', 
        city_id=6,
        description="Ever since the Eurostar undersea rail link between Paris and London rolled into Kings Cross St. Pancras station, the formerly down-and-out neighborhood of Kings Cross has experienced a total transformation. Abandoned railway land with disused gas tanks now has new offices, fountains, apartments, green spaces, and more. There are now posh supermarkets in converted train sheds, the coveted Central St. Martins London School of Art and Fashion, artisan restaurants like Caravan, and trendy ice cream shops like Ruby Violet. The space has been totally transformed  into a luxury shopping and gallery experience.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c11.jpeg",
        address="Kings Cross, London, UK",
        lat= 51.535108523501364,
        lng= -0.12467069167942887,
        duration=60,
        user_id=1
        )
    D12 = Custom_destination(
        name='Wilton\'s Music Hall', 
        city_id=6,
        description="Wilton’s Music Hall, hidden down a tiny back alley in Whitechapel, East London, is the last intact survivor of Britain’s grand music hall era. And it's beautiful. Originally built in 1859 by John Wilton and fully refurbished in 2015 to fit modern-day requirements, the venue still retains its crumbling, faded façade and peeling plaster. Any visit here—whether for a show or just for a drink at the bar—is to travel back in time to an era when entertainment was bawdy, and when dancing was an entry requirement.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c12.jpeg",
        address="1 Graces Alley, Whitechapel London, E1 8JB United Kingdom",
        lat= 51.510829425238555,
        lng= -0.06685545768318267,
        duration=60,
        user_id=1
        )
    D13 = Custom_destination(
        name='Hyde Park', 
        city_id=6,
        description="Hyde Park is big. At one and a half miles long and a mile or so wide, it's one of London's largest Royal Parks, originally appropriated from the monks at Westminster Abbey by Henry VIII to hunt deer, but now the sort of space where anything goes. Think gangs of roller-bladers on the paths, mad swimmers and chill boaters in the Serpentine Lake, rowdy protestors at Speaker’s Corner and kids aplenty riding horses and tipping their toes into the Diana Memorial Fountain.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c13.jpeg",
        address="Hyde Park, London, UK",
        lat= 51.507294890798775,
        lng= -0.16569811535498233,
        duration=60,
        user_id=1
        )
    D14 = Custom_destination(
        name='St. Paul\'s Cathedral', 
        city_id=6,
        description="One of the most famous cathedrals in the world, St. Paul's (finished in 1708) is the masterpiece of architect Sir Christopher Wren, and its towering dome is probably second on the definitive list of symbols of London after Big Ben. It's awe-inspiring, magical yet somber and reflective, a place for prayer whether you're religious or not. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c14.jpeg",
        address="St. Paul's Churchyard, London EC4M 8AD, United Kingdom",
        lat= 51.513958785576655,
        lng= -0.09835060186229297,
        duration=120,
        user_id=1
        )
    D15 = Custom_destination(
        name='Bailey House Museum', 
        city_id=8,
        description="The Bailey House Museum, a small lava rock and Koa wood home, has seen many lives. Built in 1833 as a mission, it served as a female seminary, then a private home, and then a base during World War II. Today, the museum houses Maui's largest collection of Hawaiian artifacts. There's history throughout every inch, from the well-worn doorways to the creaky floors, all of which recall a time before Maui became known as a tony resort town.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c15.jpeg",
        address="2375 Main St A Wailuku, Hawaii, 96793 United States",
        lat= 20.886380372155504,
        lng= -156.50699030243186,
        duration=60,
        user_id=1
        )
    D16 = Custom_destination(
        name='Ululani\'s Hawaiian Shave Ice', 
        city_id=8,
        description="Don't mistake proper Hawaiian shave ice with the chunky, frigid stuff you'd find at a carnival or stadium back home. Ululani's, an institution, makes its signature treat with purified water, cane sugar, purées made in-house with local fruit, and, of course, love. There are plenty of combinations to choose from, but take a hint from the name of the classic No Ka Oi (\"the Best\"), a zingy mix of mango, coconut, and passion fruit, and order wisely. Make sure to ask for a big drizzle of the coconut cream, too.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c16.jpeg",
        address="790 Front St Lahaina, Hawaii, 96761 United States",
        lat= 20.875395277598336,
        lng= -156.67952218894047,
        duration=60,
        user_id=1
        )
    D17 = Custom_destination(
        name='Brooklyn Botanic Garden', 
        city_id=9,
        description="The Brooklyn Botanic Garden is a series of gardens, pavilions, and conservatories connected by a looping path. Greenhouses hold bonsais, rare orchids, and desert plants, while outdoor spaces range from a lush Shakespeare garden to a Japanese-style lily pond traversed by a romantic bridge. Depending on the season, you might spot hot-pink peonies, cherry blossoms shedding their confetti-like petals, or stately rose bushes heavy with lush flowers.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c17.jpeg",
        address="990 Washington Ave. Brooklyn, New York, 11215 United States",
        lat= 40.66966759394487,
        lng= -73.96243464615166,
        duration=120,
        user_id=1
        )
    D18 = Custom_destination(
        name='Prospect Park', 
        city_id=9,
        description="Though not quite as famous outside of its borough, Prospect Park is in many ways the Central Park of Brooklyn; in fact, it was designed shortly after by the same team of architects, Frederick Law Olmsted and Calvert Vaux, and has many of the same features: sprawling meadows made for picnicking, walking trails that snake through dense forests, and a picturesque lake. There's also a carousel, playgrounds, a zoo, basketball and tennis courts, and a 3.35-mile loop road that's popular with runners and bikers.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/c18.jpeg",
        address="Brooklyn, NY",
        lat= 40.66035017679062,
        lng= -73.96896653080746,
        duration=120,
        user_id=1
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



    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_custom_destinations():
    db.session.execute('TRUNCATE custom_destinations RESTART IDENTITY CASCADE;')
    db.session.commit()