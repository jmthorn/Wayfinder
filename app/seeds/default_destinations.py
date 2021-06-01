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