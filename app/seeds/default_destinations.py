from app.models import db, Default_destination

# Adds a demo user, you can add other users here if you want
def seed_default_destinations():

    D1 = Default_destination(
        name='Mount Bonnell', 
        city_id=1,
        description="Mount Bonnell, also known as Covert Park, is a prominent point alongside the Lake Austin portion of the Colorado River in Austin, Texas. It has been a popular tourist destination since the 1850s.The mount provides a vista for viewing the city of Austin, Lake Austin, and the surrounding hills. It was designated a Recorded Texas Historic Landmark in 1969, bearing Marker number 6473, and was listed on the National Register of Historic Places in 2015.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d1.1.jpeg",
        address="Mt Bonnell, Austin, TX 78731",
        lat=30.321982413719372,
        lng= -97.77325451940332,
        duration=30
        )
    D2 = Default_destination(
        name='Texas State Capitol', 
        city_id=1,
        description="If it's in Texas, it must be bigger and better. That is the motto that architects followed with the Capitol Building in Austin. At one time, it was the tallest capitol building in the nation. Others might be taller now, but this is still a beautiful building that shows off many of the natural resources which are so prevalent in Texas, such as limestone and the landscapes.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d2.1.jpeg",
        address="1100 S Congress Ave, Austin, TX 78704-1728",
        lat= 30.253491428576755,
        lng= -97.74795390244505,
        duration=180
        )
    D3 = Default_destination(
        name='Lady Bird Lake Hike-and-Bike Trail', 
        city_id=1,
        description="In the heart of Austin is the Ann and Roy Butler Hike-and-Bike Trail at Lady Bird Lake, a lush, urban path that meanders along the water’s edge and passes by skyscrapers, neighborhoods, ball fields and cultural attractions. With the completion of the Boardwalk portion of the Trail in June 2014, the 1.3 mile gap along the south shore has been closed, and the Trail now serves our city in an additional way – as an alternative transportation route for our growing urban core.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/3.1.jpeg",
        address="Ann and Roy Butler Hike and Bike Trail, Austin, TX",
        lat=30.25924009716859,
        lng= -97.74361154477457,
        duration=120
        )
    D4 = Default_destination(
        name='Barton Springs Pool', 
        city_id=1,
        description="Barton Springs Pool is a recreational outdoor swimming pool that is filled entirely with water from nearby natural springs. It is located on the grounds of Zilker Park in Austin, Texas. The pool exists within the channel of Barton Creek and utilizes water from Main Barton Spring, the fourth largest spring in Texas.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/4.1.jpeg",
        address="2201 Barton Springs Rd Zilker Park, Austin, TX 78746-5736",
        lat=30.263847899088887,
        lng= -97.77072147984568,
        duration=120
        )
    D5 = Default_destination(
        name='Blanton Museum of Art', 
        city_id=1,
        description="The Jack S. Blanton Museum of Art at the University of Texas at Austin is one of the largest university art museums in the U.S. with 189,340 square feet devoted to temporary exhibitions, permanent collection galleries, storage, administrative offices, classrooms, a print study room, an auditorium, shop, and cafe.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/5.1.jpeg",
        address="200 E Martin Luther King Jr Blvd, Austin, TX 78712",
        lat=30.281176617091877,
        lng= -97.73748063127977,
        duration=120
        )
    D6 = Default_destination(
        name='Franklin Barbecue', 
        city_id=1,
        description="A standout star within Austin’s heavyweight barbecue scene, Franklin draws lines that are as epic as its world-renowned brisket. Take a tip from the regulars: come early, come hungry, and come with a collapsible chair (you don't want to stand for three or four hours if you can avoid it). Just don’t miss that luscious oak-smoked brisket with its distinctive peppery exterior; it’s tender enough to cut with a spoon. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/6.1.jpeg",
        address="900 E 11th St, Austin, TX 78702",
        lat=30.270310836585907,
        lng= -97.73119834292794,
        duration=120
        )
    D7 = Default_destination(
        name='Laguna Gloria', 
        city_id=1,
        description="The Contemporary Austin - Laguna Gloria, formerly known as the AMOA-Arthouse at Laguna Gloria, is the former home of Clara Driscoll and site of a 1916 Italianate-style villa on the shores of Lake Austin in Austin, Texas. It was the original home of the Austin Museum of Art and still houses some of its collections.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/7.1.jpeg",
        address="3809 W 35th St, Austin, TX 78703",
        lat=30.31225638878753,
        lng= -97.77432200244392,
        duration=90
        )
    D8 = Default_destination(
        name='"I Love You So Much" Mural', 
        city_id=1,
        description="Located on buzzing South Congress Avenue, on one side of the popular Jo's Coffee, it's a green painted wall bearing a simple message in elegant red text: \"I love you so much\". You don't need tickets, but you will almost certainly need to wait your turn in line for a few minutes to have a photograph taken (that's where Jo's Coffee comes in handy - try the signature TURBO: a sweet, chocolatey iced coffee that Austinites swear by).",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/8.1.jpeg",
        address="1300 S. Congress Ave.",
        lat=30.249568237770504,
        lng= -97.74940244477476,
        duration=30
        )
    D9 = Default_destination(
        name='Zilker Botanical Garden', 
        city_id=1,
        description="The Zilker Botanical Garden is a botanical garden of varied topography located on the south bank of the Colorado River at 2220 Barton Springs Road, near downtown Austin, Texas, United States. The Botanical Garden was established as a non-profit organization in 1955, and is the centerpiece of Zilker Park.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/9.jpeg",
        address="2220 Barton Springs Rd, Austin, TX 78746",
        lat=30.268976634592487,
        lng= -97.77147873127997,
        duration=150
        )
    D10 = Default_destination(
        name='Central Machine Works', 
        city_id=1,
        description="Central Machine Works is a big, airy beer hall and microbrewery in east Austin. It has a light, bright warehouse vibe (it's a converted machine works, hence the name). Picture one big, expansive space with high ceilings, enormous windows and deep leather sofas to sink into as you sample their pleasantly extensive beer menu.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/10.jpeg",
        address="4824 E Cesar Chavez St, Austin, TX 78702",
        lat=30.252124427103283,
        lng= -97.70158853128031,
        duration=120
        )

    D11 = Default_destination(
        name='Runyon Canyon Park', 
        city_id=2,
        description="Just two blocks from Hollywood Boulevard, Runyon Canyon Park is an often-overlooked urban park that offers some great views. The park boasts several hiking trails and is a popular spot for celebrities to exercise. During your hike, you'll see plenty of palm trees. Atop the canyon, you'll be treated to sweeping views of the San Fernando Valley.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/11.jpeg",
        address="2000 N Fuller Ave, Los Angeles, CA 90046",
        lat=34.10552347562681,
        lng= -118.34915740240488,
        duration=120
        )
    D12 = Default_destination(
        name='Griffith Observatory and Griffith Park', 
        city_id=2,
        description="Griffith Observatory sits on the south face of Mount Hollywood and overlooks the Los Angeles basin. Its location gives visitors impressive views of the surrounding area, which many rave about. But there's more than just a pretty photo-op here. The observatory hosts fascinating exhibitions and features a top-notch planetarium.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/12.jpeg",
        address="2800 E Observatory Rd, Los Angeles, CA 90027",
        lat=34.1191846221185,
        lng= -118.3002647563803,
        duration=120
        )
    D13 = Default_destination(
        name='The Getty Center', 
        city_id=2,
        description="The Getty Center is one of the most impressive architectural achievements in the United States – and it also contains some of the finest works of art in the world. The circular concrete-and-steel structure was designed by renowned architect Richard Meier, and it houses an abundance of art from various ages and nations. Here you'll find Renaissance paintings, 20th-century American photography, Baroque sculptures, historic manuscripts and more, all housed inside a sprawling, modern campus amid the Santa Monica Mountains. The museum also offers spectacular views of Los Angeles on clear days.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/13.jpeg",
        address="1200 Getty Center Dr, Los Angeles, CA 90049",
        lat=34.078155747299974,
        lng= -118.47407394473348,
        duration=120
        )
    D14 = Default_destination(
        name='Los Angeles County Museum of Art', 
        city_id=2,
        description="The Los Angeles County Museum of Art is an art museum located on Wilshire Boulevard in the Miracle Mile vicinity of Los Angeles. LACMA is on Museum Row, adjacent to the La Brea Tar Pits. LACMA was founded in 1961, splitting from the Los Angeles Museum of History, Science and Art.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/14.jpeg",
        address="5905 Wilshire Blvd, Los Angeles, CA 90036",
        lat=34.06415892195596,
        lng= -118.35921857356894,
        duration=120
        )
    D15 = Default_destination(
        name='The La Brea Tar Pits and Museum', 
        city_id=2,
        description="La Brea Tar Pits are a group of tar pits around which Hancock Park was formed in urban Los Angeles. Natural asphalt has seeped up from the ground in this area for tens of thousands of years. The tar is often covered with dust, leaves, or water. Over many centuries, the tar preserved the bones of trapped animals.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/15.jpeg",
        address="5801 Wilshire Blvd, Los Angeles, CA 90036",
        lat=34.06393988828396,
        lng= -118.35545605354349,
        duration=120
        )
    D16 = Default_destination(
        name='Walt Disney Concert Hall', 
        city_id=2,
        description="The Walt Disney Concert Hall at 111 South Grand Avenue in downtown Los Angeles, California, is the fourth hall of the Los Angeles Music Center and was designed by Frank Gehry. It opened on October 24, 2003. Bounded by Hope Street, Grand Avenue, and 1st and 2nd Streets, it seats 2,265 people and serves, among other purposes, as the home of the Los Angeles Philharmonic orchestra and the Los Angeles Master Chorale.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/16.jpeg",
        address="111 S Grand Ave, Los Angeles, CA 90012",
        lat=34.055528762945116,
        lng= -118.24981820211967,
        duration=30
        )
    D17 = Default_destination(
        name='Universal Studios Hollywood', 
        city_id=2,
        description="Get ready for the ultimate Hollywood experience! Find a full day of action-packed entertainment all in one place: thrilling theme park rides and shows, a real working movie studio, and Los Angeles’ best shops, restaurants and cinemas at CityWalk. Universal Studios Hollywood is a unique experience that’s fun for the whole family.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/17.jpeg",
        address="100 Universal City Plaza, Universal City, CA 91608",
        lat=34.13828106264068,
        lng= -118.35336757356698,
        duration=240
        )
    D18 = Default_destination(
        name='Stahl House', 
        city_id=2,
        description="The Stahl House is a modernist-styled house designed by architect Pierre Koenig in the Hollywood Hills section of Los Angeles, California, which is known as a frequent set location in American films.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/18.jpeg",
        address="1635 Woods Dr, West Hollywood, CA 90069",
        lat=34.10069618789019,
        lng= -118.37029130240327,
        duration=45
        )
    D19 = Default_destination(
        name='The Last Bookstore', 
        city_id=2,
        description="A diverse selection of titles spans two floors, the second of which is a labyrinth of wonder; tunnels and passageways are made of old books, interspersed with art and riveting tales. For seven years, The Last Bookstore has existed within a historic bank building, drawing repeat visits from locals and curious tourists alike.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/19.jpeg",
        address="453 South Spring Street Ground Floor, Los Angeles, CA 90013",
        lat=34.047769652655475,
        lng= -118.24961723123982,
        duration=30
        )
    D20 = Default_destination(
        name='Cathedral of Our Lady of the Angels', 
        city_id=2,
        description="The Cathedral of Our Lady of the Angels (Spanish: Catedral de Nuestra Señora de los Ángeles), informally known as COLA or the Los Angeles Cathedral, is a cathedral of the Roman Catholic Church in Los Angeles, California, United States. It opened in 2002 and serves as the mother church for the Archdiocese of Los Angeles, as well as the seat of Archbishop José Horacio Gómez.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/20.jpeg",
        address="555 W Temple St, Los Angeles, CA 90012",
        lat=34.05790369587742,
        lng= -118.24491970055793,
        duration=60
        )
    D21 = Default_destination(
        name='Chihuly Garden and Glass', 
        city_id=3,
        description="Located in the heart of Seattle, Chihuly Garden and Glass provides a look at the inspiration and influences that inform the career of artist Dale Chihuly. Through the exhibition’s eight interior galleries, lush outdoor garden and centerpiece Glasshouse visitors will experience a comprehensive look at Chihuly's most significant series of work.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/21.jpeg",
        address="305 Harrison St, Seattle, WA 98109",
        lat=47.62067196942624,
        lng= -122.35047978849416,
        duration="120"
        )
    D22 = Default_destination(
        name='Pike Place Fish Market', 
        city_id=3,
        description="Pike Place Market is a special community within the heart of Seattle’s downtown. More than the city’s beloved public market, Pike Place Market is a vibrant neighborhood comprised of hundreds of farmers, craftspeople, small businesses and residents. Each group is an important and vital makeup of the Pike Place Neighborhood. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/22.jpeg",
        address="86 Pike Pl, Seattle, WA 98101",
        lat=47.60892301372364,
        lng= -122.34047855108288,
        duration=120
        )
    D23 = Default_destination(
        name='Space Needle', 
        city_id=3,
        description="The Space Needle is an observation tower in Seattle, Washington, United States. Considered to be an icon of the city and the Pacific Northwest, it has been designated a Seattle landmark. Located in the Lower Queen Anne neighborhood, it was built in the Seattle Center for the 1962 World's Fair, which drew over 2.3 million visitors. Nearly 20,000 people a day used its elevators during the event.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/23.jpeg",
        address="400 Broad St, Seattle, WA 98109",
        lat=47.62066899091317,
        lng= -122.3492130289773,
        duration=120
        )
    D24 = Default_destination(
        name='Discovery Park', 
        city_id=3,
        description="Discovery Park is a 534-acre park on the shores of Puget Sound in the Magnolia neighborhood of Seattle, Washington. It is the city's largest public park and contains 11.81 miles of walking trails. United Indians of All Tribes' Daybreak Star Cultural Center is within the park's boundaries.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/24.jpeg",
        address="3801 Discovery Park Blvd, Seattle, WA 98199",
        lat=47.662130722976826,
        lng= -122.43564550016922,
        duration=180
        )
    D25 = Default_destination(
        name='Seattle Meowtropolitan', 
        city_id=3,
        description="Open since January, 2016, Meowtropolitan is located in Seattle’s Fremont district, across Lake Union just north of downtown.  The cafe has an ideal set-up with a separate full-service coffee shop and cat lounge.  Both rooms have an outstanding loft-like atmosphere, with marbled effect concrete floors, lots of wood, dark bricks and exposed ductwork.  The coffee room is more dark and atmospheric, while the light in the cat lounge is bright and cheerful, owing to the large picture windows that flank the bench seating. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/25.jpeg",
        address="1225 N 45th St, Seattle, WA 98103",
        lat=47.66137893816357,
        lng= -122.34293765965751,
        duration=30
        )
    D26 = Default_destination(
        name='Seattle Public Library', 
        city_id=3,
        description="The Seattle Public Library is the public library system serving the city of Seattle, Washington. Efforts to start a Seattle library had commenced as early as 1868, with the system eventually being established by the city in 1890.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/26.jpg",
        address="1000 4th Ave, Seattle, WA 98104",
        lat=47.61723579310513,
        lng= -122.33450025422428,
        duration=60
        )
    D27 = Default_destination(
        name='Washington Park Arboretum UW Botanic Gardens', 
        city_id=3,
        description="Washington Park is a public park in Seattle, Washington, United States, most of which is taken up by the Washington Park Arboretum, a joint project of the University of Washington, the Seattle Parks and Recreation, and the nonprofit Arboretum Foundation.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/27.jpeg",
        address="2300 Arboretum Dr E, Seattle, WA 98112",
        lat=47.640337449506134,
        lng= -122.29441685784028,
        duration=120
        )
    D28 = Default_destination(
        name='Fremont Troll', 
        city_id=3,
        description="The Troll was constructed in 1990 after winning a Fremont Arts Council competition for designs to improve the freeway underpass, which then was a dumping ground. He was sculpted by Steve Badanes, along with two of his University of Washington architecture students, Will Martin and Ross Whitehead, and Steve’s then-girlfriend Donna Walter.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/28.jpeg",
        address="N 36th St, Seattle, WA 98103",
        lat=47.651780407736275,
        lng= -122.34773751551042,
        duration="30"
        )
    D29 = Default_destination(
        name='The Gum Wall', 
        city_id=3,
        description="The Market Theater Gum Wall is a brick wall covered in used chewing gum located in an alleyway in Post Alley under Pike Place Market in Downtown Seattle. Much like Bubblegum Alley in San Luis Obispo, California, the Market Theater Gum Wall is a local landmark.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/29.jpeg",
        address="1428 Post Alley, Seattle, WA 98101",
        lat=47.60848726219204,
        lng= -122.34031674431854,
        duration=30
        )
    D30 = Default_destination(
        name='Old Stove Brewing', 
        city_id=3,
        description="The entire 80-foot western window wall of our space opens completely, allowing for guests to soak up fantastic views of Elliot Bay, the Olympic Mountains, and marine traffic while enjoying a fresh craft drink and a delicious meal made to order. Sunsets are a particularly great time to visit when the entire space fills with a golden northwest light just before the sun drops behind the Olympic Mountain Range. It’s truly a sight (and a beer) to behold.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/30.jpeg",
        address="1901 Western Ave, Seattle, WA 98101",
        lat=47.60947226025094,
        lng= -122.34273265965938,
        duration=120
        )
    D31 = Default_destination(
        name='Nyang Nyang Beach', 
        city_id=4,
        description="In Bali, the words “south” and “secluded” are rarely uttered in the same sentence, but Nyang Nyang Beach, in Uluwatu, indeed fills the bill. White sands, greenery-lined cliffs, and the astonishing absence of crowds await—if you're dedicated enough to find it. Who knows, you might get lucky and have the coast all to yourself. If you’ve lamented how overrun Bali’s main beaches have become nowadays, Nyang Nyang is the respite you’ve been looking for.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/31.jpeg",
        address="Pantai Nyang Nyang, Bali, Indonesia",
        lat=-8.8450225075423,
        lng= 115.11099854383724,
        duration=240
        )
    D32 = Default_destination(
        name='Gunung Kawi Temple', 
        city_id=4,
        description="Gunung Kawi is an 11th-century complex of courtyards and cliff-carved shrines along the Pakerisan River, near Ubud. Theories and myths surround the ancient Hindu site—legend has it that a ferocious warrior named Kebo Iwa carved the intricate reliefs with his fingernails, for instance—which adds to its allure. Getting down to this jungle-enshrouded marvel will require some serious walking (there are some 300 steps), but the reward—especially in the quieter morning hours—is immense.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/32.jpeg",
        address="Banjar Penaka, Tampaksiring, Kabupaten Gianyar, Bali, 80552, Indonesia",
        lat=-8.422661864235252,
        lng= 115.31274390831521,
        duration=180
        )
    D33 = Default_destination(
        name='Banyu Wana Amertha Waterfall', 
        city_id=4,
        description="Banyu Wana Amertha Waterfall, a recently opened Northern Bali attraction, is a little hard to get to. You'll need to drive at least 90 minutes from Ubud and take a winding, 20-minute hike through a banana plantation. But once you've completed the journey, you'll be rewarded handsomely with a lush forest hiding a quartet of grand waterfalls that are somehow not overrun by crowds. The main waterfall is the most spectacular—a verdant rock amphitheater with misty streams cascading down to a shallow pool.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/33.jpeg",
        address="Jl. Bhuana Sari, Bali, 81161, Indonesia",
        lat=-8.218919100202495,
        lng= 115.1217488683262,
        duration=240
        )
    D34 = Default_destination(
        name='Pura Lempuyang Luhur', 
        city_id=4,
        description="Located far from the tourist hubbub of Ubud, Lempuyang Temple is a sacred seven-temple complex in eastern Bali best known for the Gateway to Heaven that perfectly frames the formidable Mount Agung, the island’s tallest peak. This is one of the most majestic sights in Bali—come for sunrise for the best, least crowdede results—and it’s also a significant Hindu temple. Entrance requires a donation, a sarong (also available on loan), and a 40,000 rupiah ($3) round-trip jeep shuttle up the steep mountainside.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/34.jpeg",
        address="Desa Lempuyang, Seraya Bar., Kec. Karangasem, Kabupaten Karangasem, Bali, 80852, Indonesia",
        lat=-8.3911652305242,
        lng= 115.631150197373,
        duration=300
        )
    D35 = Default_destination(
        name='Tukad Cepung Waterfall', 
        city_id=4,
        description="Tukad Cepung, located in East Bali, is one of the island’s most photogenic falls, a small site leaving a major impression on travelers willing to scale the numerous steps and crossings to see it. The trump card here is drawcard is the natural light show which occurs in the earlier portion of the day. Arrive mid- to late morning for less crowded encounters, as snap-happy tourists start to flood the area by noon.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/35.jpeg",
        address="Tembuku, Tembuku, Kabupaten Bangli, Bali, 80671, Indonesia",
        lat=-8.402360375537281,
        lng= 115.38939974734187,
        duration=240
        )
    D36 = Default_destination(
        name='Ubud Monkey Forest', 
        city_id=4,
        description="This tourist magnet might look like an open-air zoo attraction, but Ubud Monkey Forest is actually a holy site with a 1000-plus band of long-tailed Balinese macaques in their natural habitat. As cantankerous as some of the monkeys can be—dangling jewelry, bags, and conspicuous food will invite aggressive sticky fingers—the primates are considered sacred by Balinese Hindus who come to pray in the complex's three ancient temples.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/36.jpeg",
        address="Kecamatan Ubud, Kabupaten Gianyar, Bali, 80571, Indonesia",
        lat=-8.515714643475068,
        lng= 115.25848697940228,
        duration=240
        )
    D37 = Default_destination(
        name='Beji Guwang Hidden Canyon', 
        city_id=4,
        description="Beji Guwang Hidden Canyon, a Sukawati-based ravine and sacred Balinese site, feels hidden in plain sight. Beyond the ticketed entrance is a series of mid-rise canyons lining the Oos River: prepare to climb, wade, swim, and scale your way through a rocky-tropical landscape not seen anywhere else on the island. Guides are necessary for safety and if possible, avoid rainy season as the currents can rise to dangerous levels—the canyon closes on days when it’s especially hazardous.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/37.jpeg",
        address="Jalan Sahadewa, Banjar Wangbung, Guwang, Sukawati, Guwang, Kec. Sukawati, Kabupaten Gianyar, Bali, 80582, Indonesia",
        lat=-8.609724351070023,
        lng= 115.28941786854011,
        duration=180
        )
    D38 = Default_destination(
        name='Tegalalang Rice Terrace', 
        city_id=4,
        description="Tegalalang Rice Terrace, 20 minutes north of Ubud, is one of Bali’s most photogenic—and most-visited—destinations. The UNESCO World Heritage Site contains wide, undulating layers of rice paddies, kept alive by an ancient, sophisticated irrigation system and farmers who tend the terraces just as previous generations have done for millennia. You can explore this area freely. Take a short stroll or navigate its entire length; descend to some of the lower slopes (if the farmers don’t mind) for a different vantage point; or grab a seat at an open-air cafe when you need a break.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/38.jpeg",
        address="Jl. Raya Tegallalang, Tegallalang, Kec. Tegallalang, Kabupaten Gianyar, Bali, 80561, Indonesia",
        lat=-8.455484837405812,
        lng= 115.27890761086807,
        duration=180
        )
    D39 = Default_destination(
        name='Sekumpul Waterfall', 
        city_id=4,
        description="If exploring Bali’s paradiscal scenery is a priority, a visit to Sekumpul Waterfall is practically essential. It is considered by many to be the island’s finest waterfall destination. Like most North Bali waterfalls, accessing Sekumpul will require some sweat. It’ll take around an hour to walk the trails and make your way down the verdant ravine, but once you do you'll be rewarded with a vast expanse of idyllic tropical landscapes, and grand-scale falls, which appear to pour from the heavens.  ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/39.jpeg",
        address="Sawan, Lemukih, Sudaji, Sekumpul Sekumpul Village, Singaraja, Bali, 81112, Indonesia",
        lat=-8.115847880497627,
        lng= 115.096988583015,
        duration=180
        )
    D40 = Default_destination(
        name='Tirta Gangga', 
        city_id=4,
        description="Although Tirta Gangga ($2 entry), a former palace turned lavish water gardens, looks like it has existed for several centuries, it was actually conceived in 1946 by the royal Karangasem family. But its far-reaching east Bali location hasn’t stopped travelers from exploring its magical fountains, shrubs, sculptures, and flowers, or positioning themselves on the octagonal stepping stones and feeding the carp. There are also stone spring water pools and you can even swim in one of them.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/40.jpeg",
        address="Jalan Raya Abang Desa Adat, Ababi, Abang, Kabupaten Karangasem, Bali, 80852,  Indonesia",
        lat=-8.410670770587474,
        lng= 115.5872112835549,
        duration=240
        )
    D41 = Default_destination(
        name='Shinjuku Gyoen National Garden', 
        city_id=5,
        description="Fancy a stroll in a Japanese garden? Get that and more at Shinjuku Gyoen. In addition to native, traditional gardens, the 144-acre park pockets French Formal and English Landscape gardens, all of which are worth the modest entrance fee. Landmarks are stunning and impossible to forget, like a Taiwan Pavilion perched along a serene pond. Formerly an imperial garden, it became a national garden after World War II—so you can trust that this precious plot is always beautifully maintained. Don't miss cherry blossom season.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/41.jpeg",
        address="11 Naitomachi, Shinjuku City, Tokyo, 160-0014, Japan",
        lat=35.685411566770235,
        lng= 139.710040968833,
        duration=180
        )
    D42 = Default_destination(
        name='Yayoi Kusama Museum', 
        city_id=5,
        description="In a suburban part of Shinjuku, a smooth white building rises five stories high—a museum completely devoted to the works of Yayoi Kusama. The building looks slim, but it houses a bulk of the larger-than-life and avant-garde artist's pieces, including a new installation of her “infinity room” series (an Instagram sensation which, in the past, drew hundreds of thousands of visitors in stateside exhibitions) to polka-dotted paintings and sculptures. Currently, to reduce the spread of coronavirus, entry is limited to 40 people per 90-minute admission slot.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/42.jpeg",
        address="107 Bentencho, Shinjuku City, Tokyo, 162-0851, Japan",
        lat=35.70342330360877,
        lng= 139.7264603399981,
        duration=180
        )
    D43 = Default_destination(
        name='Senso-ji', 
        city_id=5,
        description="Tokyo may not have as many temples as Kyoto, but Senso-ji isn't the city's most popular just by default. The atmosphere alone here is one for the bucket list. Senso-ji, the temple itself, is at the end of the shopping street, while a recently renovated five-story pagoda stands to the left (ranking in as the second tallest pagoda in Japan). Japanese visitors flutter around a large cauldron in front of the temple where incense burned inside is said to benefit good health. Travelers keen to avoid crowds should arrive early, but even tourists that are remotely interested in Japanese culture will find something to appreciate here.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/43.jpeg",
        address="2 Chome-3-1 Asakusa, Tokyo, 111-0032, Japan",
        lat=35.713494305103424,
        lng=139.79516238232793 ,
        duration=120
        )
    D44 = Default_destination(
        name='Tsukiji Market', 
        city_id=5,
        description="In October 2018, the world's largest fish market, Tsukiji, shut down after 83 years and re-opened in two distinct parts. At the original location, it's pretty much business as usual, with street-food stalls serving up everything from seared tuna to uni sandwiches in squid-ink sticky buns. Just down the road at Toyosu Market, meanwhile, you can taste fresh raw fish in a series of sushi bars and peek in on the auctions (formerly held at Tsukiji) and live fish sales from a second-story viewing station. You can also tour a large green space on the rooftop, which affords views of the Tokyo skyline.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/44.jpeg",
        address="5 Chome-2-1 Tsukiji, Chuo City, Tokyo, 104-0045, Japan",
        lat=35.66464072890329,
        lng= 139.7692473283492,
        duration=180
        )
    D45 = Default_destination(
        name='Golden Gai', 
        city_id=5,
        description="This clutch of narrow streets, tucked in the shadows of Shinjuku, is lined with hundreds of low-slung dive bars with just a handful of seats, all recalling post-war debauchery. There's no order to the scene, and considering that bars are stacked—some at ground level, while some are located up steep, svelte staircases—it's just as fascinating to wander aimlessly as it is to arrive with a game plan. Recently, the area has gained popularity among visitors, so don’t be surprised if several of your fellow tipplers hail from abroad. Many of the bars frequented by locals require a seating charge, so check before ordering a drink. Albatross and Ace’s are welcoming spaces that cater to a mixed crowd, and there’s no cover charge. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/45.jpeg",
        address="1 Chome-1-6 Kabukicho, Shinjuku City, Tokyo, 160-0021, Japan",
        lat=35.69428762037983,
        lng= 139.704767068833,
        duration=180
        )
    D46 = Default_destination(
        name='Nakameguro', 
        city_id=5,
        description="It's okay to visit the artsy neighborhood, Nakameguro, just to see its seasonal appeal as one of the most picture-perfect spots for cherry blossoms in Spring. However, stick around these charming streets and you'll find a hip collection of independent cafes and boutiques that offer a laid-back alternative to the city's buzzing hubs. Sakura trees hug the Meguro River in Nakameguro's center, blossoming as they lean over the sloped, canal-like walls surrounding the water. Once you've taken a moment to smell the blossoms (and fill your phone with pitcures), you'll find an array of independent boutiques and cafés branching off along narrow streets in either direction. Head to the corner-side Onibus Coffee, which serves single-origin espresso, and stop at SML, a boutique stocking delightful crafts (especially ceramics) made by Japanese artists. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/46.jpeg",
        address="Meguro City, Tokyo, 153-0061, Japan",
        lat=35.63931468839211,
        lng= 139.70485796089753,
        duration=240
        )
    D47 = Default_destination(
        name='Nezu Museum', 
        city_id=5,
        description="This serene museum in the Aoyama district, redesigned by celebrated architect Kengo Kuma, is a contemporary temple for traditional art. A long, covered outdoor path alongside bamboo-clad walls serves as a minimalist entrance, but once inside, double-height interiors and glass walls stretch over 40,000 square feet while keeping the experience intimate. And while the museum mixes contemporary design and traditional art on the inside—over 7,400 pieces—the outside counts, too: The property is home to a stunning private garden that's worth the visit all on its own. The bulk of the museum's art was once the private collection of Nezu Kaichirō, the president of Japan's Tobu Railway. Since the midcentury, the collection grew and now comprises over 7,400 pieces.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/47.jpeg",
        address="Minami-Aoyama 6-5-1, Minato-ku, Tokyo, 107-0062, Japan",
        lat=35.66238753259357,
        lng= 139.71709369766762,
        duration=180
        )
    D48 = Default_destination(
        name='Sumo at Ryogoku Kokugikan', 
        city_id=5,
        description="Only three of six official grand tournaments happen in Tokyo, all at Ryogoku Kokugikan. The stadium houses over 11,000 eager fans under its green, pavilion-style roof. Official tournaments last just over two weeks each, which means Ryogoku Kokugikan sometimes hosts other events (boxing, for example). But sumo is the arena's feature attraction, and if you're hoping to see sumo in Tokyo, this is where to find it. To prevent the spread of COVID-19, the 2021 grand tournament will take place with reduced audiences, and spectators will be required to wear masks.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/48.jpeg",
        address="1 Chome-3-28 Yokoami, Sumida City, Tokyo, 130-0015, Japan",
        lat=35.69738413145225,
        lng= 139.7924045246572,
        duration=120
        )
    D49 = Default_destination(
        name='Yoyogi Park', 
        city_id=5,
        description="Yoyogi Park is one of the most amusing parks in Tokyo. Its 134 acres sprawl right in Shibuya, a short skip from Harajuku, and bustle with picnics and performers. The northern side is lush, with clean walkways along expansive, grassy lawns where locals and tourists spread under the shade of Japanese Zelkova trees, and gather around a large pond. Spot impromptu badminton team swinging racquets, a drum circle tapping away at the bongo, or amateur dancers following along to the beat.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/49.jpeg",
        address="2-1 Yoyogikamizonocho, Shibuya City, Tokyo, 151-0052, Japan",
        lat=35.6695093851586,
        lng= 139.70138301300844,
        duration=180
        )
    D50 = Default_destination(
        name='Omoide Yokocho', 
        city_id=5,
        description="Shinjuku's Omoide Yokocho is an atmospheric, narrow lane filled with 60 or so bustling, open-fronted hole in-the-wall restaurants, each seating only a handful of customers. Even at these small yakitori joints, you can embrace the Japanese concept of omakase, where you leave your meal in the hands of the chefs. Then sit back and relax while you are served a continuous stream of tasty skewers of chicken, pork, and vegetables.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/50.jpeg",
        address="1 Chome-2 Nishishinjuku, Tokyo, 160-0023, Japan",
        lat=35.69313564960353,
        lng= 139.6995510399978,
        duration=120
        )
    D51 = Default_destination(
        name='National Gallery', 
        city_id=6,
        description="Set in London’s busiest open space, Trafalgar Square, this is the grandmother of galleries with more than 2,300 paintings spanning the 13th to the 19th centuries (Heavyweights include Van Gogh’s Sunflowers, Velequez’s Rokeby Venus, and Constable’s six-foot long The Hay Wain). It gets packed at weekends, but its so large that you can usually find a quiet corner. Download one of the myriad audio tour options and explore. You can download an audio tour covering the museum's highlights, but you can also curate your own by selecting the paintings you want to see before you arrive.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/51.jpeg",
        address="Trafalgar Square, London, WC2N 5DN, United Kingdom",
        lat=51.5090625304149,
        lng=-0.12832045964859304,
        duration= 180
        )
    D52 = Default_destination(
        name='The Globe Theater', 
        city_id=6,
        description="In London, every building and street has history. And Shakespeare's Globe, although a reconstruction of the original Globe Theatre—where many of William Shakespeare's plays were first staged and which burned down in 1613 during a performance of 'Henry VIII'—is no exception. The theater was rebuilt not far from its original site, using construction methods and materials as close to the original as possible, and to watch a performance here is to step back in time with the Royal Shakespeare Company.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/52.jpeg",
        address="21 New Globe Walk, London, SE1 9DT, United Kingdom",
        lat=51.50826500945794,
        lng= -0.09716031546860657,
        duration= 180
        )
    D53 = Default_destination(
        name='Tower of London', 
        city_id=6,
        description="Built by William the Conqueror in 1066, this uncompromising slab of a building has been many things—including the site where Henry VIII ordered the execution of two of his wives. Now the Tower is most famous as the home of the Crown Jewels. Come, take a tour from one of the Beefeaters (offered every half hour), and gawp at the sparkling and the frightening alike.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/53.jpeg",
        address="St Katharine's & Wapping, London, EC3N 4AB, United Kingdom",
        lat=51.508272643396076,
        lng= -0.07588492896058675,
        duration=120
        )
    D54 = Default_destination(
        name='Columbia Road Flower Market', 
        city_id=6,
        description="Weekly on Sundays, Columbia Road in East London's hip Shoreditch/Hackney neighborhood, transforms into a multicolored frenzy of stalls and flowers. This otherwise unassuming East End street is transformed into a swath of magnificent plant life, the air fragrant with blooms and the shouts of historic London's famous Cockney stallholders. It's as eccentric as it gets around here. You'll hear rushed deals and offers for a 'tenner' or 'fiver' (ten or five pounds) and because everything is so fresh, it's all gotta be gone by 2 p.m. ",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/54.jpeg",
        address="Columbia Rd., London, E2 7RG, United Kingdom",
        lat=51.52926914576562,
        lng= -0.06983045964773821,
        duration=30
        )
    D55 = Default_destination(
        name='British Museum', 
        city_id=6,
        description="You could spend several lifetimes in the British Museum, Britain’s largest museum, without running out of artifacts to ponder. The collection is one of the largest in the world, arranged by location (Ancient Egypt, Asia, Africa, the Middle East, and Greece and Rome), and the list of big hitters includes the Rosetta Stone and other finds from Ancient Egypt, Asia and the Middle East. Come early on a weekday for a less crowded experience, pick one gallery and stick to it (or go for a guided “Highlights” tour), and plan to hit one of the day’s free 30-minute taster talks.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/55.jpeg",
        address="Great Russell St., London, WC1B 3DG, United Kingdom",
        lat=51.51954901912368,
        lng= -0.12694832764078462,
        duration=180
        )
    D56 = Default_destination(
        name='The Shard', 
        city_id=6,
        description="Western Europe's tallest building at 309.6 metres, or 1,016 feet, high, The Shard houses London's first Shangri-la hotel, private apartments, offices and three high-end restaurants – Aqua Shard, Hutong and Oblix. All good reasons to visit of course but arguably the main one is the viewing gallery aka The View. Located on floors 68-72 and 244 meters above London, you have an unobstructed 360-degree, 40-mile view across the city.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/56.jpeg",
        address="32 London Bridge St., London, SE1 9SG, United Kingdom",
        lat=51.504666934275626,
        lng= -0.08640344245272925,
        duration=90
        )
    D57 = Default_destination(
        name='Hawksmoor', 
        city_id=6,
        description="I feel naughty descending the stairs into Hawksmoor’s cavernous underground space for their legendary Sunday roast and a Bloody Mary or three. Naughty because the parquet flooring, exposed brick walls, low lighting and the fact it doubles as a neighborhood cocktail bar for Covent Garden’s locals makes it feel more hidden drinking den than posh restaurant. Plus the heady smells of steak coming from the kitchen go to your head. And let's be clear: Hawksmoor's food is commonplace let's be clear—steak/fries/booze with a little lobster thrown in—but the difference is they do it bloody well and serve with class.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/57.jpeg",
        address="11 Langley St., London, WC2H 9JG, United Kingdom",
        lat=51.513612901498,
        lng= -0.1257967308124053,
        duration= 60
        )
    D58 = Default_destination(
        name='Borough Market', 
        city_id=6,
        description="The food hound's favorite London market (and the city's most atmospheric) occupies a sprawling site near London Bridge, both in a large covered area and spreading into the smaller maze of streets that surround it. Records show there’s been a market here since 1276 when it apparently caused traffic jams on London Bridge. What’s on offer? Gourmet goodies run the gamut and you’d be hard pressed not to find something you can’t get enough of and simply spend all day stuffing your face.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/58.jpeg",
        address="8 Southwark St., London, SE1 1TL, United Kingdom",
        lat=51.505481253319495,
        lng= -0.09109794173932238,
        duration=120
        )
    D59 = Default_destination(
        name='Hampstead Heath', 
        city_id=6,
        description="Forget the perfect lawns of London's Royal Parks, Hampstead Heath, the vast and, in places wonderfully overgrown, tract of countryside just north of the rock ‘n’ roll neighborhood of Camden Town is the wild heart of the city and an undisputed highlight, so much so it's said to have inspired CS Lewis’s Narnia. The Heath covers 791 acres of woodland, playing fields, swimming ponds and meadows of tall grass perfect both for picnickers and couples in search of privacy. It’s truly beautiful.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/59.jpeg",
        address="Hampstead Heath, London, United Kingdom",
        lat=55.54918960925105,
        lng= 0.1975010267139666,
        duration=240
        )
    D60 = Default_destination(
        name='Highgate Cemetery', 
        city_id=6,
        description="A graveyard is always a somber place, but Highgate is also a celebratory one. You’ll recognize parts of it if you’ve seen Francis Ford Coppola’s ‘Dracula,’ and you'll find the final resting place of writers like George Eliot and Douglas Adams, science pioneers like Michael Faraday and pop culture icons like George Michael (although his grave isn't yet open to the public). And believe it or not, for somewhere with so many legendary men and women buried in it, Highgate Cemetery is one of the least visited of London’s landmarks. But those who do come for both the ghostly mystery of the place itself, as well as fans of the celebrity dead.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/60.jpeg",
        address="Swain's Ln., London, N6 6PJ, United Kingdom",
        lat=51.5681541673458,
        lng= -0.14724256335014926,
        duration=120
        )
    D61 = Default_destination(
        name='Camps Bay Beach', 
        city_id=7,
        description="Camps Bay is Cape Town's party beach: A beautiful, long stretch of white sand bordered by a promenade full of restaurants, clubs, and hotels for when you need a break from the sun. It's fun and lively and can feel a bit crowded—and, fine, maybe a bit tacky—during the peak summer months of December and January. But the setting is absolutely gorgeous, with the Twelve Apostles mountain range making for a craggy backdrop. Amid the loud beach bars you'll find some dining gems, so it's definitely worth a stop.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/61.1.jpeg",
        address="Camps Bay Beach, Cape Town, 8005, South Africa",
        lat=-30.779335463588588,
        lng=18.008667008486544,
        duration= 180
        )
    D62 = Default_destination(
        name='Zeitz Museum of Contemporary Art Africa', 
        city_id=7,
        description="The Zeitz MOCAA is one of the most important new museums in the global art world: It's the first-ever major institution dedicated exclusively to artists from across the African continent and diaspora. It's also a must-see for architecture buffs; the building, a reimagining of an abandoned silo building, was designed by UK starchitect Thomas Heatherwick. The result is a soaring, sculptural marvel that really is a work of art in itself. It's modern and industrial, and Capetonians are rightly proud of the new landmark building.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/62.jpeg",
        address="Zeitz Museum of Contemporary Art Africa, V&A Waterfront Silo District, S Arm Rd, Waterfront, Cape Town, 8001, South Africa",
        lat=-31.53030866304981,
        lng= 18.382730798942546,
        duration= 90
        )
    D63 = Default_destination(
        name='The Neighbourgoods Market', 
        city_id=7,
        description="Neighbourgoods Market, in Woodstock, is a pioneering market for South Africa; since its inception in 2006, there's been a boom in markets taking over disused spaces in vibrant urban enclaves across the country. But Neighbourgoods remains the one to beat: There's a diverse range of food stalls from around the world, serving ostrich burgers to paella to dim sum, and local artisans sell their fresh jams, cheeses, and biltong (jerky) alongside. As you navigate the entire complex, with live musicians playing in the background, you'll also find a warren of stalls by emerging designers selling chic dresses, sunglasses, hats, and jewelry.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/63.jpeg",
        address="373 Albert Rd, Woodstock, Cape Town, 7925, South Africa",
        lat=-31.127074123482725,
        lng= 17.943232302093573,
        duration=120
        )
    D64 = Default_destination(
        name='Lion\'s Head', 
        city_id=7,
        description="The neighbor to the much more formidable Table Mountain, Lion's Head is no shrinking violet: The striking conical spire adds a distinctive quirk to Cape Town's skyline. While many like to hike both, Lion's Head is a much quicker and easier climb, and the trail wraps around on its way to the top, which means your view is constantly changing—just what you need to keep you energized when you start to feel winded. And best of all, Table Mountain makes up part of your view.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/64.jpeg",
        address="Lion's Head, Signal Hill, Cape Town, 8001, South Africa",
        lat=-31.680745865870257,
        lng= 18.541691167047524,
        duration=180
        )
    D65 = Default_destination(
        name='Greenmarket Square', 
        city_id=7,
        description="This lively spot is more about soaking in the ambience rather than sourcing quality goods. One of South Africa's most historic markets—the cobbled square was set up in the late 1600s—Greenmarket is now a bustling flea with vendors selling everything from colorful wall hangings and paintings to necklaces to toys, all while musicians supply a festive soundtrack. It's the kind of place you can expect to bargain a bit, but within reason, of course, and afterward stroll to one of countless cute area cafés set in old heritage buildings for a cappuccino.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/65.jpeg",
        address="Burg St &, Longmarket St, Cape Town City Centre, Cape Town, 8000, South Africa",
        lat=-31.380750783054506,
        lng=  18.20571062739321,
        duration=60
        )
    D66 = Default_destination(
        name='Cape of Good Hope', 
        city_id=7,
        description="No trip to Cape Town is complete without the half-day Cape Peninsula drive, heading to the southwesternmost point of the African continent. This is where European ships rounded Africa en route to the east, and thanks to the rocky shores and temperamental waters, many never made it past. It's now a nature reserve, where you can go on hikes, climb up to the lighthouse at Cape Point, and pose with a sign at the Cape of Good Hope. Along the way, you'll likely spot some animals by the side of the road.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/66.jpeg",
        address="Cape Point Rd, Cape Town, 8001, South Africa",
        lat=-31.84171247660735,
        lng= 18.583734640866272,
        duration=240
        )
    D67 = Default_destination(
        name='Robben Island Museum', 
        city_id=7,
        description="This island, about five miles off the coast of Cape Town, had been a notorious penal colony since the Dutch and English colonial times. But its main notoriety comes from the fact that this is where many iconic South African freedom fighters were imprisoned—chief among them Nelson Mandela, who spent 18 years of his 27-year sentence at Robben Island. Visitors board a ferry from the V&A Waterfront (they should book in advance, as boats frequently sell out), then take a bus tour around the island before walking through the prison itself.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/67.jpeg",
        address="Robben Island, Cape Town, 7400, South Africa",
        lat=-33.7988711821586,
        lng= 18.372199671345605,
        duration= 180
        )
    D68 = Default_destination(
        name='Table Mountain', 
        city_id=7,
        description="It's practically impossible to find a spot in Cape Town that's not in the shadow of Table Mountain: This majestic plateau dominates the city's skyline and makes a photogenic backdrop to virtually any picture. But people don't just gaze upon it; you can scale the stately 3,500-foot-tall behemoth in many ways. Choose from any number of hiking trails—they range from challenging to near death-defying, so choose wisely—or, if you're the more easy-going (read: lazy) type, take the cable car up and down in five minutes flat each way.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/68.jpeg",
        address="Maclear's Beacon, Table Mountain (Nature Reserve), Cape Town, South Africa",
        lat=-30.930683349009453,
        lng= 18.384172786968612,
        duration=240
        )
    D69 = Default_destination(
        name='Kirstenbosch National Botanical Garden', 
        city_id=7,
        description="This is one of our favorite places in Cape Town: a beautiful, serene expanse on the slopes of Table Mountain, with more than 7,000 plant species, most of which are unique to this part of the world (keep an eye out for all kinds of proteas, birds of paradise, wild gardenia, and much more). Scattered throughout the 1,300 acres are various artwork and sculptures, and in summer the park hosts concerts and events against the stunning mountain backdrop.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/69.jpeg",
        address="Rhodes Dr, Newlands, Cape Town, 7735, South Africa",
        lat=-31.83164340881742,
        lng= 18.21194986552304,
        duration=240
        )
    D70 = Default_destination(
        name='District Six Museum', 
        city_id=7,
        description="District Six was a vibrant, mixed-race community in Cape Town until its residents were forcibly evicted by the apartheid government in the 1970s. The original residents have dispersed far and wide, and now this intimate museum stands as a memorial to them. The entire collection of the two-story venue is created from personal artifacts from former residents: pictures, artwork, letters, news clippings, and narrations recorded on tape. While it's certainly not off the beaten path, it makes for a poignant counterpart to Robben Island, allowing you to understand some of what common people endured during apartheid.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/70.jpeg",
        address="25A Buitenkant St, Zonnebloem, Cape Town, 8000, South Africa",
        lat=-31.380889005859764,
        lng= 18.38327035863844,
        duration=120
        )
    D71 = Default_destination(
        name='Road to Hana', 
        city_id=8,
        description="The curvaceous Road to Hana, which hugs Maui's northeastern shore around Haleakalā National Park, is one of the island's most memorable experiences, one that will make the hassle of renting a car worth it. The 52-mile road harks back to a Hawaii before shopping malls and crowds, with 59 bridges to cross—46 of which have only one lane. The trip can easily take a full day, two if you stay overnight. It's a feast for the senses as well, with plenty to see as you stop along the way. Whatever you do, be sure to visit one of the many roadside stands that sell fresh fruit, smoothies, hand-carved Koa wood mementos, and—best of all—warm banana bread.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/71.jpeg",
        address="Hana, HI 96713",
        lat=20.76020765866085,
        lng=-155.98785183937224,
        duration= 60
        )
    D72 = Default_destination(
        name='Haleakalā National Park', 
        city_id=8,
        description="The highest point on Maui is also one of its most visited: Haleakalā Crater provides epic, sweeping views of the island from an elevation of just over 10,000 feet. The visitor center is a great place to start, whether you're driving up in a rental car, opting for a sunrise van tour, or getting a little more adventurous with a backpacking trip on the famous Sliding Sands Trail. Come prepared with an extra layer—weather at this elevation can change drastically. At sunrise in the middle of summer, the temperature at the summit is likely to hover around 50 degrees Fahrenheit.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/72.jpeg",
        address="Haleakala Hwy Kula, Hawaii, 96790 United States",
        lat=20.786616609357008,
        lng= -156.30655421407224,
        duration= 200
        )
    D73 = Default_destination(
        name='Feast at Lele', 
        city_id=8,
        description="Don't come to the Feast at Lele expecting plastic leis, screaming children, and a sad buffet line; rather, this is a quintessential Maui luau without the cheesiness. The five-course dinner (served at private tables—a rarity on the luau scene) pairs live performances with cuisine from four different Pacific island regions: first Hawaii, then Aotearoa (New Zealand), Tahiti, and Samoa. Then comes dessert. The food is great. Standouts include a five-hour braised beef with kiwi jus from New Zealand. Come hungry—the portions are large and you won't want to miss out on the final note: a vanilla-coconut-lime mousse cake with caramelized pineapple.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/73.jpeg",
        address="505 Front St Lahaina, Hawaii, 96761 United States",
        lat=20.868119837729154,
        lng= -156.6752084601044,
        duration=120
        )
    D74 = Default_destination(
        name='Kula Botanical Garden', 
        city_id=8,
        description="What began in 1977 as a native plant reserve has transformed into Kula Botanical Garden, one of upcountry Maui's most beloved attractions, visited by thousands every year. Thanks to its location on the slopes of Haleakalā, the rich volcanic soil provides fertile ground for a great variety of plants, each labeled and many native to Maui. Admission is only $10 for adults—a fair price to pay to view more than 2,000 plants.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/74.jpeg",
        address="638 Kekaulike Ave Kula, Hawaii, 96790 United States",
        lat=20.742301421004424,
        lng= -156.32545757545088,
        duration=60
        )
    D75 = Default_destination(
        name='Makena Cove', 
        city_id=8,
        description="Tucked between a few houses and behind a stone wall, the oasis of Makena Cove has a real feeling of discovery to it. Although most visitors are familiar with Makena Beach just to the north, very few take the extra steps to this gorgeous outcrop where volcanic rock meets the sea in spectacular fashion. The waves are dramatic, the crowds are nonexistent, and the sense of adventure is real. Come for a sunset mid-week and you're likely to have the place pretty much to yourself.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/75.jpeg",
        address="6468 Makena Alanui Kihei, Hawaii, 96753",
        lat=20.640743667964355,
        lng= -156.4438828447635,
        duration=180
        )
    D76 = Default_destination(
        name='Pipiwai Trail', 
        city_id=8,
        description="It's about the journey, not the destination, right? On the Pipiwai Trail, it's about both. The remote trail is about 12 miles past Hana town on the Road To Hana. There are bamboo forests, a well-maintained trail, and not one, but two waterfalls. And at just about four miles roundtrip, it's a doable hike for people of all ages. As part of the Kīpahulu District inside Haleakalā National Park, you can expect a clean trail, beautifully maintained bridges, boardwalks, and rock steps. Make sure to stop for a breather in the bamboo forests—the sounds of bamboo trees clicking against each other in the wind is the kind of chilling nature moment people seek when they come to Maui. About three-fourths of the way through, you'll encounter the 185-foot Makahiku Falls which is, crazily, small potatoes compared to the 400-foot Waimoku Falls where the trail concludes.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/76.jpeg",
        address="42222 Hana Hwy Hāna, Hawaii, 96713 United States",
        lat=20.66534491814718,
        lng= -156.04227801592705,
        duration=180
        )
    D77 = Default_destination(
        name='Ho\'okipa Beach Park', 
        city_id=8,
        description="Located miles away from the crowds, this pristine beach is nestled on the island's north shore alongside the Road To Hana. Thanks to its consistent winds, large waves, and sprawling reef system, this is one of Hawaii's best spots for windsurfing. Keep an eye out for the abundance of honu (green sea turtles). Many people miss these mystical sea creatures, especially as they blend in with the numerous exposed reefs and rocks along the beach. In the early evening, they tend to emerge from the sea to rest and, perhaps, to watch the beautiful sunsets. Maui institution Mama's Fish House is just down the road, so you can fuel up on locally-caught fish tacos and lobster tails after a day on the beach.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/77.jpeg",
        address="179 Hana Highway Paia, Hawaii, 96779 United States",
        lat=20.917687477567316,
        lng= -156.38013826010356,
        duration= 180
        )
    D78 = Default_destination(
        name='Wailea Golf Club', 
        city_id=8,
        description="The Wailea Golf Club is one of the world's great golf destinations. Three distinct courses offer a variety of terrain and challenges, keeping pros raving and avid amateurs coming back year after year to better their game. The Wailea Emerald course has fabulous ocean views from every hole. The Wailea Blue's location, in the foothills of Haleakalā, provide a uniquely challenging course with unforgettable vistas over the island's largest dormant volcano.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/78.jpeg",
        address="100 Wailea Golf Club Drive Wailea, Hawaii, 96753 United States",
        lat=20.675988018257225,
        lng= -156.43437344661592,
        duration=220
        )
    D79 = Default_destination(
        name='D.T. Fleming Park', 
        city_id=8,
        description="With food, amenities, soft sand, and approachable waves, this is the perfect beach for families. The waves can be aggressive on occasion, but generally the water is safe. It's adjacent to the Ritz Carlton and Kapalua resorts, so it's not one of Maui's more remote beaches, but that's not why you come here. It has everything you need, from restrooms complete with outdoor rinse showers, a burger shack for a snack, plenty of knowledgable lifeguards, barbecue grills, picnic tables, a payphone (hey, who knows what you might need), and ironwood trees in case you need a bit of shade. Go for a swim, bring the kids, float around, and let loose. This is carefree Hawaii at its best.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/79.jpeg",
        address="Lower Honoapiilani Rd Lahaina, Hawaii, 96761 United States",
        lat=20.976147714162195,
        lng= -156.6772740447581,
        duration=240
        )
    D80 = Default_destination(
        name='Blue Hawaiian Helicopters', 
        city_id=8,
        description="Everyone who walks away from a Blue Hawaiian helicopter tour calls it a must-do experience on Maui—the choppers fill up fast, so be sure to reserve in advance. Departing from Kahului, Blue Hawaiian then lifts you up and away for a 65-minute loop around the island's perimeter. You're in for views that can only be seen from the sky—each tour promises volcanos, soaring oceanfront cliffs, cascading waterfalls, rugged coastline, and lush valleys, many of which aren't accessible any other way, with plenty of commentary from knowledgable pilots.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/80.jpeg",
        address="1, Lelepio Pl, Kahului, HI 96732",
        lat=20.89471627927804,
        lng= -156.43087926808,
        duration=120
        )
    D81 = Default_destination(
        name='Brooklyn Bridge', 
        city_id=9,
        description="When the Brooklyn Bridge was constructed in 1883—extending 1,595 feet across the East River, connecting lower Manhattan to Brooklyn Heights—it was the longest suspension bridge in the world. Now, it’s a historic staple of the New York City skyline, transporting commuter car traffic underneath and touristic foot traffic above. Standing before arches and rectangles with city skyscrapers rising in the distance, will at once inspire a sense of grandiosity and slightness.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/81.jpeg",
        address="Furman St., Pier 1 Brooklyn, New York , 11201 United States",
        lat=40.7034705315703,
        lng=-73.99523826916747,
        duration= 180
        )
    D82 = Default_destination(
        name='The High Line', 
        city_id=9,
        description="The High Line is a perfect example of what New York City does best: cleverly rehabs old spaces into exactly what you want them to be. When a 1.45-mile-long abandoned freight rail on Manhattan’s West End was transformed into an elevated, mixed-use public park in 2009, New Yorkers came running. Towering 30 feet above buzzing 11th Avenue, the High Line is a masterful feat of landscape architecture that melds walkways, benches, and chaise lounges with grass, perennials, trees, and bushes in perfect unkempt-kempt harmony.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/82.jpeg",
        address="New York, NY 10011",
        lat=40.748104065723915,
        lng=  -74.0047223401129,
        duration= 180
        )
    D83 = Default_destination(
        name='Central Park', 
        city_id=9,
        description="Step off the crowded sidewalks of 59th Street into Central Park and you’ll hardly realize what lies before you: 693 acres of man-made gardens, meadows, forests, and rolling hillsides. If you ambled down every one of Central Park’s pathways, you would walk 58 miles. Along the way, you pass fountains, monuments, sculptures, bridges, and arches, plus 21 playgrounds, a winter ice-skating rink, a zoo, and even a castle. But you’d hardly notice the four major crosstown thoroughfares, which cleverly disappear into foliage-covered tunnels.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/83.jpeg",
        address="Fifth Ave. and 59th St. New York, New York, 10019 United States",
        lat=40.78124616234897,
        lng= -73.96652091828314,
        duration=120
        )
    D84 = Default_destination(
        name='The Cloisters', 
        city_id=9,
        description="Located on four acres in northern Manhattan's Fort Tryon Park, the Met Cloisters is a branch of the Metropolitan Museum of Art and is America’s only museum dedicated exclusively to the art and architecture of the Middle Ages. The building overlooks the Hudson River and actually incorporates five medieval-inspired cloisters into a modern museum structure, creating a historic, contextualized backdrop in which to view the art.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/84.jpeg",
        address="99 Margaret Corbin Dr. New York, New York, 10040 United States",
        lat=40.86522348073598,
        lng= -73.93176764429302,
        duration=120
        )
    D85 = Default_destination(
        name='Whitney Museum of American Art', 
        city_id=9,
        description="The Whitney got a major upgrade when it relocated from the Upper East Side to its vastly-expanded Meatpacking headquarters in 2015. It houses 50,000 square feet of indoor galleries with works by Jean Michel Basquiat, Richard Avedon, and Alexander Calder, four outdoor exhibition spaces and terraces, and a ground-floor restaurant and top-floor bar, both by Danny Meyer, one of the town’s best-known restaurateurs. The floors are connected by two artist-designed elevators (albeit slow-moving, crowded ones). If mobility isn’t an issue, take the stairs instead, which offer uninterrupted views of the Hudson river. The upper floors and sculpture terraces are also connected by a series of exterior staircases, with great views of the downtown skyline, and a rare opportunity to experience art en plein aire.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/85.jpeg",
        address="99 Gansevoort St. New York, New York, 10014 United States",
        lat=40.73973594417336,
        lng= -74.00898233080517,
        duration=180
        )
    D86 = Default_destination(
        name='The Metropolitan Museum of Art', 
        city_id=9,
        description="For nearly a century and a half, the Met has remained the cultural epicenter of New York City, thanks to forward-thinking exhibits and an extensive permanent collection. With its Gothic-Revival-style building, iconic tiered steps, and Central Park location, the building is a sight to be seen. But step inside its Great Hall—as a ceaseless parade of museumgoers move to-and-fro—and you’ll feel the overwhelming sense of possibility and discovery that lays beyond. If you've got limited time or compatriots with limited attention spans, start with the Temple of Dendur, a 2,000-year-old soaring Egyptian temple (the only complete one in the Western Hemisphere)",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/86.jpeg",
        address="1000 Fifth Ave. New York , New York , 10028 United States",
        lat=40.779303590995454,
        lng=-73.9628956154594,
        duration=120
        )
    D87 = Default_destination(
        name='The Morgan Library & Museum', 
        city_id=9,
        description="The Morgan is like a multi-hyphenate millennial—only instead of actress/model/influencer/whatever, it’s museum/library/landmark/historic site/music venue. Inside the multimillionaire’s personal library, expanded into a must-see museum and cultural space, you'll find rare artifacts, paintings, and books, some dating back to 4000 B.C. that are worth more than your house. In particular the museum is home to one of 23 copies of the original Declaration of Independence; Mozart's handwritten score of the Haffner Symphony; the collected works of African American poet Phillis Wheatley; the only extant manuscript of Milton's Paradise Lost; and Charles Dickens’s manuscript of A Christmas Carol. Swoon.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/87.jpeg",
        address="225 Madison Ave. New York, New York, 10016 United States",
        lat=40.74933129752125,
        lng= -73.98152650196863,
        duration= 60
        )
    D88 = Default_destination(
        name='Statue of Liberty', 
        city_id=9,
        description="In 2019 4.2 million tourists visited Liberty Island, the 14-acre swath of land one mile south of lower Manhattan where the Statue of Liberty rests. While there is no fee to visit Liberty Island, you do have to pay for a round-trip ferry ride via Statue Cruises. The ferry also stops on Ellis Island, part of the national park, which houses the Ellis Island National Museum of Immigration, where visitors can search ship manifests for the records of their relatives. If you plan to visit the Statue’s pedestal or crown, plan ahead: There are a limited number of tickets available each day and they sell out weeks, if not months, in advance. Also plan on spending the day: It can six hours to properly visit the statue and Ellis Island.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/88.jpeg",
        address="Liberty Island New York, New York, 10004 United States",
        lat=40.68962579843671,
        lng= -74.04492383262573,
        duration=120
        )
    # D89 = Default_destination(
    #     name='9/11 Memorial and Museum', 
    #     city_id=9,
    #     description="Every American should visit the 9/11 Memorial and Museum at least once. As you enter the museum, you descend from the street to bedrock level—the foundation of the former Twin Towers—and are placed in a meditative mindset, forced to recall where you were on that fateful day. The museum itself is a masterful balance: It's grand in scale, contemplative in its construction, and personal in its execution. It pays homage to the enormity of the loss, both physical and spiritual.",
    #     image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/89.jpeg",
    #     address="180 Greenwich St. New York, New York, 10007 United States",
    #     lat=40.71156106425868,
    #     lng= -74.01245714429756,
    #     duration=180
    #     )
    D90 = Default_destination(
        name='Rockefeller Center', 
        city_id=9,
        description="Rockefeller Center sits in the heart of midtown Manhattan, both in terms of its physical location and its prominent place in the city's folklore and culture. Whether you want to check out a performance on the plaza outside the TODAY show, visit the Christmas tree, or practice your best moves on the ice skating rink, you're in for an iconic, family-friendly experience. If you buy a ticket to Top of the Rock, you'll enjoy spectacular views of the city below. No matter where you are, you're bound to be constantly pointing and shouting “hey, look at that!”",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/90.jpeg",
        address="45 Rockefeller Plaza New York, New York, 10111 United States",
        lat=40.75980276459208,
        lng= -73.97869008662386,
        duration=80
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
    db.session.add(D51)
    db.session.add(D52)
    db.session.add(D53)
    db.session.add(D54)
    db.session.add(D55)
    db.session.add(D56)
    db.session.add(D57)
    db.session.add(D58)
    db.session.add(D59)
    db.session.add(D60)
    db.session.add(D61)
    db.session.add(D62)
    db.session.add(D63)
    db.session.add(D64)
    db.session.add(D65)
    db.session.add(D66)
    db.session.add(D67)
    db.session.add(D68)
    db.session.add(D69)
    db.session.add(D70)
    db.session.add(D71)
    db.session.add(D72)
    db.session.add(D73)
    db.session.add(D74)
    db.session.add(D75)
    db.session.add(D76)
    db.session.add(D77)
    db.session.add(D78)
    db.session.add(D79)
    db.session.add(D80)
    db.session.add(D81)
    db.session.add(D82)
    db.session.add(D83)
    db.session.add(D84)
    db.session.add(D85)
    db.session.add(D86)
    db.session.add(D87)
    db.session.add(D88)
    # db.session.add(D89)
    db.session.add(D90)


    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_default_destinations():
    db.session.execute('TRUNCATE default_destinations RESTART IDENTITY CASCADE;')
    db.session.commit()