# import libraries
import streamlit as st
import pandas as pd
import numpy as np
from bokeh.models.widgets import Div
import pickle
import csv
from time import strftime
from joblib import load

from recommendation import project_recommendation

#load model
# filename = 'final_model.sav'
# model = pickle.load(open(filename, 'rb'))

#useful functions
def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, email):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write('DateStamp={}, Name={}, Email={} \n'.format(timestamp, name, email))
    data.close()

def model_run(data):
    x_tst = pd.DataFrame(data)
    print(x_tst)
    model= load("rf_final.joblib")
    y_pred = model.predict(x_tst)

    return y_pred

## Main Page details:
st.markdown("<h1 style='color: SteelBlue;'>KickStarter Crowdfunding Recomendation Engine</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='margin: 0px 0px 0px 0px;'>Idea</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'>Kickstarter is one of the most popular crowdfunding platform on the internet. The aim of this project is to predict the success or failure of a Kickstarter campaign at launch time.</p>", unsafe_allow_html=True)
st.markdown("<h2 style='margin: 0px 0px 0px 0px;'>Abstract</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'>Crowdfunding is the practice of funding a project or venture by raising monetary contributions from many people. The majority of today’s crowdfunding happens online through various websites and one of the most prominent is Kickstarter. The steps to start a Kickstarter project are; start a campaign, set the minimum funding goal, set reward levels, and choose a deadline. The most important aspect to know about launching a Kickstarter project is that if the project falls short of meeting its minimum funding goal, the project will not receive any fund. The projects analyzed in this project fall into one of 14 categories and 51 subcategories. Only 55% of campaigns reach their funding goal thus it is extremely important for creators to know the factor(s) that might impact the outcome of their project before launch.</p>", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'><br>This project will take inputs from users using website and machine learning algorithms will provide various prediction / recommendations which are helpful to conduct the crowdfunding project.</br></p>", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'><br>Input from the Users on Website / Predictor for ML Algorithm</br></p>", unsafe_allow_html=True)
st.markdown("<ul><li>Category and Subcategory of Project</li><li>Goal in Dollars</li><li>Location of the Project (City and State)</li><li>Levels, Duration and No. of Update for the Projects</li></ul>", unsafe_allow_html=True)

if st.button('Go to GitHub'):
    js = "window.open('https://github.com/shaishav11/Kickstarter-Crowdfunding-Recommendation-Engine')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

if st.button('Go to Tableau'):
    js = "window.open('https://public.tableau.com/profile/shaishav.shah#!/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


## Sidebar details
st.sidebar.markdown("<h2 style='text-align: left'>KickStarter Crowdfunding Prediction Demo</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: left'>Enter your project details:</h3>", unsafe_allow_html=True)

title = st.sidebar.text_input("Enter name for the project?")
description = st.sidebar.text_input("Enter project description?")
cat = st.sidebar.selectbox( 'Select the category of the project?', ('Select Category', 'Art', 'Comics', 'Dance', 'Design', 'Fashion', 'Film & Video', 'Film &amp; Video', 'Food', 'Games', 'Music', 'Photography', 'Publishing', 'Technology', 'Theater'))
if cat=='Select Category':
	sub_cat = st.sidebar.text_input( 'Select the Sub category of the project?', 'Select Sub Category')	
	cat=10000
	sub_cat = 10000
if cat=='Art': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Art', 'Conceptual Art', 'Digital Art', 'Illustration', 'Mixed Media', 'Painting', 'Performance Art', 'Public Art', 'Sculpture'))
	cat=0
if cat=='Comics': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', (('Select Sub Category','Comics')))
	cat=1
if cat=='Dance': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', (('Select Sub Category','Dance')))
	cat=2
if cat=='Design': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Crafts', 'Design', 'Graphic Design', 'Product Design'))
	cat=3
if cat=='Fashion': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Fashion'))
	cat=4
if cat=='Film & Video': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Categgory','Animation', 'Documentary', 'Film &amp; Video', 'Narrative Film', 'Short Film', 'Webseries'))
	cat=5
if cat=='Film &amp; Video': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Animation', 'Documentary', 'Film &amp; Video', 'Narrative Film', 'Short Film', 'Webseries'))
	cat=6
if cat=='Food': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Food'))
	cat=7
if cat=='Games': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Board & Card Games', 'Board &amp; Card Games', 'Games', 'Video Games'))
	cat=8
if cat=='Music': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Classical Music', 'Country & Folk', 'Country &amp; Folk', 'Electronic Music', 'Hip-Hop', 'Indie Rock', 'Jazz', 'Music', 'Pop', 'Rock', 'World Music'))
	cat=9
if cat=='Photography': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Photography'))
	cat=10
if cat=='Publishing': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Nonfiction', 'Fiction', 'Art Book', 'Journalism', 'Poetry',
       'Publishing', "Children's Book", 'Periodical'))
	cat=11
if cat=='Technology': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Technology', 'Open Software', 'Open Hardware'))
	cat=12
if cat=='Theater': 
	sub_cat = st.sidebar.selectbox( 'Select the Sub category of the project?', ('Select Sub Category','Theater'))
	cat=13

state = st.sidebar.selectbox( 'Select the state for your project?', ('Select City', 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))
if state== 'Select City':
	city = st.sidebar.text_input( 'Select the city for the project?', 'Select City')	
	state=10000
	city = 10000
if state=="AK": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Aleutians West', 'Anchorage', 'Barrow', 'Beluga', 'Bristol Bay', 'Deadhorse', 'Delta Junction', 'Denali', 'Fairbanks', 'Homer', 'Hoonah', 'Juneau', 'Kenai', 'Kodiak', 'Kwethluk', 'Nome', 'North Pole', 'Prudhoe Bay', 'Russian Mission', 'Sand Point', 'Sitka', 'Soldotna', 'Talkeetna', 'Unalakleet', 'Wasilla', 'Wrangell'))
	state=0
if state=="AL": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alabaster', 'Albertville', 'Andalusia', 'Anniston', 'Athens', 'Auburn', 'Bay Minette', 'Birmingham', 'Chelsea', 'Daphne', 'Decatur', 'Dothan', 'Elkmont', 'Evergreen', 'Fairhope', 'Florence', 'Fort Payne', 'Greensboro', 'Guntersville', 'Hoover', 'Huntsville', 'Jacksonville', 'Loxley', 'Madison', 'Mobile', 'Montgomery', 'Muscle Shoals', 'Pell City', 'Phenix City', 'Piedmont', 'Prattville', 'Sheffield', 'Tuscaloosa', 'Waverly', 'Wilsonville'))
	state=1
if state=="AR": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Arkadelphia', 'Batesville', 'Benton', 'Bentonville', 'Bethel Heights', 'Clarendon', 'Conway', 'El Dorado', 'Eureka Springs', 'Farmington', 'Fayetteville', 'Forrest City', 'Fort Smith', 'Greenbrier', 'Hot Springs', 'Jacksonville', 'Jonesboro', 'Kingsland', 'Little Rock', 'Malvern', 'Mountain Home', 'North Little Rock', 'Northwest', 'Pine Bluff', 'Rogers', 'Russellville', 'Sherwood', 'Siloam Springs', 'Texarkana', 'Ward'))
	state=2
if state=="AZ": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Apache Junction', 'Arizona City', 'Benson', 'Bisbee', 'Buckeye', 'Cave Creek', 'Chandler', 'Chino Valley', 'Coconino', 'Cornville', 'Cottonwood', 'Eloy', 'Flagstaff', 'Fountain Hills', 'Gilbert', 'Glendale', 'Globe', 'Grand Canyon', 'Hualapai', 'Jerome', 'Kingman', 'Lakeside', 'Litchfield Park', 'Littlefield', 'Marble Canyon', 'Maricopa', 'Mayer', 'Mesa', 'Nogales', 'Page', 'Patagonia', 'Payson', 'Peoria', 'Phoenix', 'Pinetop', 'Prescott', 'Prescott Valley', 'Queen Creek', 'Rimrock', 'Ruby', 'Sahuarita', 'San Carlos', 'Scottsdale', 'Sedona', 'Sells', 'Show Low', 'Sierra Vista', 'St Johns', 'Superior', 'Surprise', 'Taylor', 'Tempe', 'Tucson', 'Young', 'Yuma'))
	state=3
if state=="CA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Acton', 'Adelanto', 'Agoura Hills', 'Alameda', 'Albany', 'Alhambra', 'Aliso Viejo', 'Alturas', 'Alum Rock', 'American Canyon', 'Anaheim', 'Angwin', 'Antioch', 'Apple Valley', 'Aptos', 'Arcadia', 'Arcata', 'Atascadero', 'Atlanta', 'Auburn', 'Avalon', 'Azusa', 'Bakersfield', 'Barstow', 'Belmont', 'Benicia', 'Berkeley', 'Beverly Hills', 'Big Bear', 'Big Bear Lake', 'Big Pine', 'Big Sur', 'Bishop', 'Blue Lake', 'Bodega', 'Bolinas', 'Boonville', 'Boyes Hot Springs', 'Brawley', 'Brea', 'Brentwood', 'Burbank', 'Burlingame', 'Calabasas', 'California City', 'Camarillo', 'Cameron Park', 'Campbell', 'Campo', 'Canoga Park', 'Canyon Country', 'Canyon Lake', 'Capistrano Beach', 'Carlsbad', 'Carmel Valley', 'Carmichael', 'Castaic', 'Castro Valley', 'Central', 'Central Coast', 'Ceres', 'Cerritos', 'Chico', 'Chino', 'Chino Hills', 'Chula Vista', 'Claremont', 'Clayton', 'Clearlake', 'Clovis', 'Colfax', 'Compton', 'Concord', 'Corona', 'Coronado', 'Corte Madera', 'Costa Mesa', 'Coulterville', 'Covina', 'Crestline', 'Culver City', 'Cupertino', 'Cypress', 'Daly City', 'Dana Point', 'Danville', 'Davis', 'Death Valley', 'Del Mar', 'Desert Hot Springs', 'Diamond Bar', 'Dinuba', 'Dixon', 'Downey', 'Dublin', 'East Los Angeles', 'East Palo Alto', 'El Cajon', 'El Centro', 'El Cerrito', 'El Dorado', 'El Monte', 'Elk Grove', 'Emeryville', 'Encinitas', 'Escondido', 'Eureka', 'Exeter', 'Fair Oaks', 'Fairfax', 'Fairfield', 'Fallbrook', 'Folsom', 'Fontana', 'Fortuna', 'Fountain Valley', 'Fremont', 'French Camp', 'Fresno', 'Fullerton', 'Garden Grove', 'Gardena', 'Gilroy', 'Glendale', 'Glendora', 'Goleta', 'Granada Hills', 'Grass Valley', 'Hacienda Heights', 'Half Moon Bay', 'Harmony', 'Hawthorne', 'Hayward', 'Healdsburg', 'Hemet', 'Hermosa Beach', 'Hesperia', 'Highland', 'Hollister', 'Hollywood', 'Hoopa', 'Huntington Beach', 'Idyllwild', 'Independence', 'Indio', 'Inglewood', 'Irvine', 'Isla Vista', 'Jamestown', 'Joshua Tree', 'Julian', 'Kentfield', 'King City', 'La Crescenta', 'La Jolla', 'La Mesa', 'La Mirada', 'La Puente', 'La Quinta', 'Ladera Ranch', 'Lafayette', 'Laguna Beach', 'Laguna Hills', 'Laguna Niguel', 'Lake Arrowhead', 'Lake Elsinore', 'Lake Forest', 'Lakewood', 'Lancaster', 'Larkspur', 'Lawndale', 'Lemoore', 'Lennox', 'Leucadia', 'Lincoln', 'Littlerock', 'Livermore', 'Lodi', 'Loma Linda', 'Lompoc', 'Long Beach', 'Loomis', 'Los Alamitos', 'Los Alamos', 'Los Altos', 'Los Angeles', 'Los Banos', 'Los Gatos', 'Loyalton', 'Lytle Creek', 'Malibu', 'Mammoth Lakes', 'Manhattan Beach', 'Manteca', 'Marina', 'Marina Del Rey', 'Martinez', 'Mendocino', 'Menlo Park', 'Merced', 'Mill Valley', 'Millbrae', 'Milpitas', 'Mission Viejo', 'Modesto', 'Mojave', 'Montebello', 'Monterey', 'Moorpark', 'Moraga', 'Moreno Valley', 'Morgan Hill', 'Morro Bay', 'Moss Landing', 'Mount Shasta', 'Mountain View', 'Mt Baldy', 'Murphys', 'Murrieta', 'Napa', 'Nevada City', 'Newbury Park', 'Newhall', 'Newman', 'Newport Beach', 'Nicasio', 'Niland', 'North Antelope Valley', 'North Hollywood', 'Northridge', 'Norwalk', 'Novato', 'Oak Park', 'Oakdale', 'Oakhurst', 'Oakland', 'Oakley', 'Occidental', 'Oceanside', 'Ojai', 'Ontario', 'Orange', 'Oroville', 'Oxnard', 'Pacific Grove', 'Pacifica', 'Palm Desert', 'Palm Springs', 'Palmdale', 'Palo Alto', 'Palos Verdes Estates', 'Pasadena', 'Paso Robles', 'Pendleton', 'Perris', 'Pescadero', 'Petaluma', 'Pinole', 'Pismo Beach', 'Pittsburg', 'Placentia', 'Placerville', 'Pleasant Hill', 'Pleasanton', 'Point Reyes Sta', 'Pomona', 'Porterville', 'Portola Valley', 'Poway', 'Prunedale', 'Quincy', 'Rancho Cucamonga', 'Rancho Palos Verdes', 'Rancho Santa Margarita', 'Redding', 'Redlands', 'Redondo Beach', 'Redway', 'Redwood City', 'Redwood Valley', 'Rialto', 'Richmond', 'Ridgecrest', 'Riverbank', 'Riverside', 'Rocklin', 'Rohnert Park', 'Roseville', 'Running Springs', 'Sacramento', 'Saint Helena', 'Salinas', 'San Anselmo', 'San Bernardino', 'San Bruno', 'San Buenaventura (Ventura)', 'San Carlos', 'San Clemente', 'San Diego', 'San Fernando', 'San Fernando Valley', 'San Francisco', 'San Gabriel', 'San Jacinto', 'San Jose', 'San Juan Capistrano', 'San Leandro', 'San Luis Obispo', 'San Marcos', 'San Mateo', 'San Pablo', 'San Pedro', 'San Rafael', 'San Ramon', 'Santa Ana', 'Santa Barbara', 'Santa Clara', 'Santa Clarita', 'Santa Cruz', 'Santa Maria', 'Santa Monica', 'Santa Nella Village', 'Santa Paula', 'Santa Rosa', 'Santa Ynez Valley', 'Sausalito', 'Sea Ranch', 'Seal Beach', 'Seaside', 'Sebastopol', 'Sequoia National Park', 'Sherman Oaks', 'Sierra Madre', 'Signal Hill', 'Silver Lake', 'Silverado', 'Simi Valley', 'Sonoma', 'Sonora', 'Soquel', 'South Lake Tahoe', 'South Pasadena', 'South San Francisco', 'Squaw Valley', 'Stanford', 'Stockton', 'Studio City', 'Sun City', 'Sunnyvale', 'Sunol', 'Tahoe City', 'Tahoe Vista', 'Tehachapi', 'Temecula', 'Thousand Oaks', 'Three Rivers', 'Tiburon', 'Tomales', 'Topanga', 'Torrance', 'Trabuco', 'Tracy', 'Truckee', 'Tujunga', 'Tulare', 'Turlock', 'Tustin', 'Twain Harte', 'Twentynine Palms', 'Twentynine Palms Morongo Valley', 'Ukiah', 'Union City', 'Upland', 'Vacaville', 'Valencia', 'Vallejo', 'Venice', 'Ventura', 'Victorville', 'View Park Windsor Hills', 'Visalia', 'Vista', 'Walnut', 'Walnut Creek', 'Walnut Grove', 'Watsonville', 'Weaverville', 'Weed', 'West Hills', 'West Hollywood', 'West Sacramento', 'Westlake Village', 'Westminster', 'Whittier', 'Winters', 'Winton', 'Woodland', 'Yorba Linda', 'Yosemite National Park', 'Yuba City', 'Yucaipa', 'Yucca Valley'))
	state=4
if state=="CO": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alamosa', 'Arvada', 'Aspen', 'Aurora', 'Battlement Mesa', 'Berthoud', 'Boulder', 'Breckenridge', 'Broomfield', 'Buena Vista', 'Carbondale', 'Castle Rock', 'Centennial', 'Colorado Springs', 'Commerce City', 'Cortez', 'Craig', 'Crested Butte', 'Crestone', 'Cripple Creek', 'Denver', 'Dillon', 'Durango', 'Edgewater', 'Edwards', 'Estes Park', 'Evergreen', 'Federal Heights', 'Fort Collins', 'Frisco', 'Gardner', 'Golden', 'Grand Junction', 'Grand Lake', 'Greeley', 'Guadalupe', 'Highlands Ranch', 'Johnstown', 'Kersey', 'Kremmling', 'Lafayette', 'Lakewood', 'Leadville', 'Littleton', 'Longmont', 'Louisville', 'Loveland', 'Lyons', 'Manitou Springs', 'Marble', 'Naturita', 'Nederland', 'Nucla', 'Pagosa Springs', 'Paonia', 'Parker', 'Pueblo', 'Pueblo West', 'Red Feather Lakes', 'Silverton', 'Snowmass', 'Springfield', 'Superior', 'Telluride', 'Thornton', 'Vail', 'Ward', 'Westminster', 'Windsor', 'Woodland Park'))
	state=5
if state=="CT": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Andover', 'Ansonia', 'Bethlehem', 'Branford', 'Bridgeport', 'Bristol', 'Canton', 'Central Manchester', 'Chester', 'Clinton', 'Cos Cob', 'Coventry', 'Cromwell', 'Danbury', 'Deep River', 'Eastford', 'Easton', 'Enfield', 'Fairfield', 'Greenwich', 'Groton', 'Guilford Center', 'Hamden', 'Hartford', 'Jewett City', 'Lakeville', 'Litchfield', 'Mansfield', 'Meriden', 'Middletown', 'Milford', 'Monroe', 'Montville', 'Morris', 'Mystic', 'Naugatuck', 'New Britain', 'New Canaan', 'New Hartford', 'New Haven', 'New London', 'New Milford', 'Newington', 'Newtown', 'Norwalk', 'Norwich', 'Old Lyme', 'Old Saybrook', 'Plainville', 'Podunk', 'Pomfret', 'Portland', 'Putnam', 'Redding', 'Ridgefield', 'Roxbury', 'Salem', 'Salisbury', 'Sandy Hook', 'Shelton', 'Sherman', 'Simsbury Center', 'Southington', 'Sprague', 'Stafford', 'Stafford Springs', 'Stamford', 'Stonington', 'Stratford', 'Tariffville', 'Tolland', 'Torrington', 'Trumbull', 'Wallingford', 'Waterbury', 'Watertown', 'West Hartford', 'West Haven', 'Westbrook', 'Weston', 'Westport', 'Wilton', 'Windsor', 'Wolcott', 'Woodbridge', 'Woodbury'))
	state=6
if state=="DC": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Washington'))
	state=7
if state=="DE": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Bethany Beach', 'Camden', 'Dagsboro', 'Dover', 'Middletown', 'New Castle', 'Newark', 'Odessa', 'Seaford', 'Wilmington'))
	state=8
if state=="FL": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alachua', 'Altamonte Springs', 'Apalachicola', 'Apopka', 'Baker', 'Beverly Hills', 'Boca Raton', 'Bonita Springs', 'Boynton Beach', 'Bradenton', 'Bushnell', 'Cape Canaveral', 'Cape Coral', 'Chipley', 'Clearwater', 'Clermont', 'Cocoa', 'Cocoa Beach', 'Coconut Creek', 'Cooper City', 'Coral Gables', 'Coral Springs', 'Crestview', 'Dade City', 'Davie', 'Daytona Beach', 'De Bary', 'De Funiak Springs', 'De Land', 'Deerfield Beach', 'Delray Beach', 'Deltona', 'Destin', 'Duck Key', 'Dunedin', 'Eastpoint', 'Edgewater', 'Eglin Afb', 'El Portal', 'Estero', 'Eustis', 'Everglades', 'Fernandina Beach', 'Flagler Beach', 'Fort Lauderdale', 'Fort Myers', 'Fort Pierce', 'Fort Walton Beach', 'Fort White', 'Frostproof', 'Gainesville', 'Greenacres', 'Gulfport', 'Haines City', 'Hallandale', 'High Springs', 'Hobe Sound', 'Hollywood', 'Homeland', 'Homosassa', 'Hudson', 'Hutchinson Island South', 'Indian Harbour Beach', 'Jacksonville', 'Jacksonville Beach', 'Jensen Beach', 'Jupiter', 'Key Biscayne', 'Key Largo', 'Key West', 'Kissimmee', 'Lake City', 'Lake Helen', 'Lake Mary', 'Lake Worth', 'Lakeland', 'Largo', 'Leesburg', 'Lehigh Acres', 'Little Havana', 'Longwood', 'Lynn Haven', 'Macclenny', 'Madeira Beach', 'Marathon', 'Margate', 'Melbourne', 'Merritt Island', 'Miami', 'Miami Beach', 'Miami Gardens', 'Miami Lakes', 'Milton', 'Miramar', 'Naples', 'New Port Richey', 'New Smyrna Beach', 'New York', 'Newberry', 'Niceville', 'North Port', 'North Redington Beach', 'Ocala', 'Oldsmar', 'Orange Park', 'Orlando', 'Ormond Beach', 'Oviedo', 'Palm Bay', 'Palm Beach', 'Palm Coast', 'Palm Harbor', 'Palmetto', 'Panama City', 'Panama City Beach', 'Pembroke Pines', 'Pensacola', 'Pinellas Park', 'Plant City', 'Pompano Beach', 'Ponce De Leon', 'Port Charlotte', 'Port Richey', 'Port Salerno', 'Port St Lucie', 'Punta Gorda', 'Quincy', 'Rockledge', 'Safety Harbor', 'Sanford', 'Sanibel', 'Sarasota', 'Seffner', 'Seminole', 'Seneca', 'South Beach', 'Southport', 'St Augustine', 'St Pete Beach', 'St Petersburg', 'Sunrise', 'Tallahassee', 'Tamarac', 'Tampa', 'Titusville', 'Trinity', 'Valrico', 'Venice', 'Vero Beach', 'Wesley Chapel', 'West Melbourne', 'West Palm Beach', 'Windermere', 'Winter Haven', 'Winter Park', 'Zephyrhills'))
	state=9
if state=="GA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Acworth', 'Albany', 'Alpharetta', 'Athens', 'Athens Clarke County', 'Atlanta', 'Atlanta Decatur', 'Augusta', 'Avondale Estates', 'Barwick', 'Bethlehem', 'Blairsville', 'Blue Ridge', 'Brunswick', 'Buckhead', 'Buford', 'Canton', 'Carrollton', 'Chickamauga', 'Clarkesville', 'Clermont', 'Cleveland', 'Columbus', 'Commerce', 'Conyers', 'Cordele', 'Covington', 'Cumming', 'Dahlonega', 'Dallas', 'Dalton', 'Dawsonville', 'Decatur', 'Douglasville', 'Duluth', 'East Point', 'Ellijay', 'Fairburn', 'Fayetteville', 'Flintstone', 'Flovilla', 'Flowery Branch', 'Forest Park', 'Gainesville', 'Griffin', 'Grovetown', 'Helen', 'Jackson', 'Jasper', 'Jersey', 'Jonesboro', 'Kennesaw', 'La Grange', 'Lawrenceville', 'Lilburn', 'Lithonia', 'Loganville', 'Macon', 'Madison', 'Marietta', 'Mc Donough', 'Milledgeville', 'Moultrie', 'Newnan', 'Norcross', 'Oxford', 'Pelham', 'Powder Springs', 'Ringgold', 'Rome', 'Roswell', 'Sandy Springs', 'Savannah', 'Smyrna', 'Snellville', 'St Marys', 'St Simons', 'Statesboro', 'Stockbridge', 'Stone Mountain', 'Sugar Hill', 'Suwanee', 'Thomasville', 'Tifton', 'Tucker', 'Tybee Island', 'Valdosta', 'Villa Rica', 'Waverly Hall', 'Waycross', 'White Plains', 'Woodstock'))
	state=10
if state=="HI": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Aiea', 'Anahola', 'Captain Cook', 'Ewa Beach', 'Haiku', 'Haleiwa', 'Hawaiian Beaches', 'Hawi', 'Hilo', 'Honokaa', 'Honolulu', 'Kahuku', 'Kahului', 'Kailua', 'Kailua Kona', 'Kamuela', 'Kapaa', 'Kapolei', 'Kawaihae', 'Keaau', 'Kihei', 'Kilauea', 'Kula', 'Lahaina', 'Laie', 'Makawao', 'Naalehu', 'Paia', 'Papaikou', 'Pearl City', 'Pearl Harbor', 'Pukalani', 'P’ÜÎ\\x81hoa', 'Waianae', 'Wailuku'))
	state=11
if state=="IA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Ackworth', 'Albert City', 'Ames', 'Bedford', 'Bettendorf', 'Brooklyn', 'Burlington', 'Cedar Falls', 'Cedar Rapids', 'Clive', 'Council Bluffs', 'Davenport', 'Decorah', 'Des Moines', 'Dubuque', 'Durant', 'Fairfield', 'Indianola', 'Iowa City', 'Keokuk', 'Lawton', 'Mason City', 'Muscatine', 'Newton', 'Ottumwa', 'Peterson', 'Richland', 'Rock Rapids', 'Sergeant Bluff', 'Sioux City', 'Storm Lake', 'Tipton', 'Urbandale', 'Waterloo', 'Waverly', 'West Des Moines', 'Windsor Heights'))
	state=12
if state=="ID": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Blackfoot', 'Boise', 'Bruneau', 'Burley', 'Council', 'Eagle', 'Emmett', 'Garden City', 'Greenleaf', 'Idaho City', 'Idaho Falls', 'Jerome', 'Ketchum', 'Lewiston', 'Meridian', 'Moscow', 'Mountain Home', 'Nampa', 'Payette', 'Pocatello', 'Rexburg', 'Sandpoint', 'Stanley', 'Twin Falls', 'Victor'))
	state=13
if state=="IL": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Addison', 'Antioch', 'Arcola', 'Arlington Heights', 'Aurora', 'Austin', 'Belvidere', 'Berwyn', 'Bethalto', 'Bloomington', 'Bolingbrook', 'Brookfield', 'Buffalo Grove', 'Bushnell', 'Byron', 'Carbondale', 'Cary', 'Champaign', 'Chicago', 'Chicago Heights', 'Chicago Metropolitan Area', 'Clarendon Hills', 'Coal City', 'Crystal Lake', 'De Kalb', 'Decatur', 'Des Plaines', 'Dixon', 'Downers Grove', 'East Peoria', 'East St Louis', 'Effingham', 'Elgin', 'Elk Grove Village', 'Elmhurst', 'Evanston', 'Fox Lake', 'Frankfort', 'Freeport', 'Geff', 'Geneva', 'Glen Ellyn', 'Glenview', 'Greenfield', 'Greenville', 'Hanover Park', 'Harrisburg', 'Harvey', 'Highland', 'Highland Park', 'Homer', 'Joliet', 'Kankakee', 'Lake Forest', 'Lake Zurich', 'Lincoln', 'Lisle', 'Lombard', 'Lyons', 'Macomb', 'Marion', 'Mc Henry', 'Moline', 'Mt Vernon', 'Mundelein', 'Naperville', 'New Lenox', 'Niles', 'Normal', 'Northern', 'Oak Park', 'Ohio', 'Olympia Fields', 'Ottawa', 'Pawnee', 'Peoria', 'Peoria Heights', 'Plainfield', 'Plano', 'Posen', 'Rock Island', 'Rockford', 'Round Lake', 'Sandwich', 'Savoy', 'Schaumburg', 'Skokie', 'South Elgin', 'Spring Valley', 'Springfield', 'St Charles', 'Sterling', 'Summit', 'Thompsonville', 'Troy', 'Tuscola', 'Union', 'Urbana', 'Vernon Hills', 'Warrenville', 'Wauconda', 'Waukegan', 'Westmont', 'Wheaton', 'Woodstock', 'Yorkville'))
	state=14
if state=="IN": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alexandria', 'Anderson', 'Angola', 'Attica', 'Auburn', 'Batesville', 'Bedford', 'Bloomington', 'Bryant', 'Carmel', 'Chesterton', 'Columbus', 'Cromwell', 'Crown Point', 'De Motte', 'Denver', 'Dyer', 'Elkhart', 'Ellettsville', 'Erie', 'Evansville', 'Fillmore', 'Fishers', 'Fort Wayne', 'Fowler', 'Franklin', 'Gary', 'Gas City', 'Georgetown', 'Goshen', 'Granger', 'Greencastle', 'Greenfield', 'Greenwood', 'Griffin', 'Hanover', 'Highland', 'Huntington', 'Indianapolis', 'Jasper', 'Jeffersonville', 'Kokomo', 'La Porte', 'Lafayette', 'Lebanon', 'Logansport', 'Madison', 'Marengo', 'Marion', 'Markle', 'Merrillville', 'Michigan City', 'Middlebury', 'Mishawaka', 'Mooresville', 'Mt Vernon', 'Mulberry', 'Muncie', 'Munster', 'Nashville', 'New Albany', 'New Harmony', 'New Haven', 'Noblesville', 'Northwest', 'Osceola', 'Pendleton', 'Peru', 'Plainfield', 'Plymouth', 'Redkey', 'Rensselaer', 'Richmond', 'Rockville', 'Rome City', 'Sellersburg', 'Shelbyville', 'South Bend', 'Terre Haute', 'Upland', 'Utica', 'Valparaiso', 'Vernon', 'Vincennes', 'Wabash', 'Washington', 'West Lafayette', 'Winona Lake', 'Yorktown'))
	state=15
if state=="KS": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Canada', 'Coffeyville', 'Great Bend', 'Greensburg', 'Hays', 'Haysville', 'Junction City', 'Kansas City', 'Lawrence', 'Leavenworth', 'Lenexa', 'Manhattan', 'Olathe', 'Overland Park', 'Parsons', 'Pittsburg', 'Prairie Village', 'Russell', 'Salina', 'Shawnee', 'Topeka', 'Udall', 'Wichita'))
	state=16
if state=="KY": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Ashland', 'Bellevue', 'Berea', 'Booneville', 'Bowling Green', 'Brandenburg', 'Burlington', 'Campton', 'Carrollton', 'Cold Spring', 'Corbin', 'Covington', 'Crestwood', 'Danville', 'Dawson Springs', 'Dayton', 'De Mossville', 'Elizabethtown', 'Flatwoods', 'Florence', 'Frankfort', 'Glasgow', 'Hawesville', 'Hazard', 'Henderson', 'Hopkinsville', 'Hyden', 'Independence', 'Jackson', 'La Grange', 'Lawrenceburg', 'Leitchfield', 'Lexington', 'Louisville', 'Maysville', 'Morehead', 'Mt Sterling', 'Murray', 'Northern', 'Paducah', 'Paintsville', 'Pikeville', 'Radcliff', 'Richmond', 'Russellville', 'Salt Lick', 'Somerset', 'Vanceburg', 'Wilmore'))
	state=17
if state=="LA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Amite City', 'Arcadia', 'Baton Rouge', 'Bogalusa', 'Bossier City', 'Boston', 'Buras', 'Chalmette', 'Covington', 'Cut Off', 'De Ridder', 'Dulac', 'Erath', 'Ferriday', 'Fort Polk', 'Hammond', 'Kentwood', 'Lafayette', 'Lake Charles', 'Leesville', 'Mandeville', 'Metairie', 'Monroe', 'Montegut', 'New Iberia', 'New Orleans', 'Port Sulphur', 'Ruston', 'Scott', 'Shreveport', 'Simsboro', 'Slidell', 'St Francisville', 'Thibodaux', 'Transylvania', 'West Monroe'))
	state=18
if state=="MA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Adams', 'Amesbury', 'Amherst', 'Aquinnah', 'Arlington', 'Ashfield', 'Ashland', 'Barnstable', 'Barnstable Town', 'Becket', 'Bedford', 'Belchertown', 'Beverly', 'Billerica', 'Boston', 'Bourne', 'Braintree', 'Brewster', 'Brighton', 'Brockton', 'Brookline', 'Buzzards Bay', 'Cambridge', 'Chatham', 'Chelmsford', 'Chelsea', 'Concord', 'Conway', 'Cotuit', 'Danvers', 'Dartmouth', 'Deerfield', 'Dudley', 'Easthampton', 'Egremont', 'Everett', 'Fall River', 'Feeding Hills', 'Fitchburg', 'Framingham', 'Franklin', 'Gardner', 'Gloucester', 'Goshen', 'Grafton', 'Granby', 'Great Barrington', 'Greenfield', 'Groton', 'Hadley', 'Hardwick', 'Harwich Center', 'Hatfield', 'Hingham', 'Holyoke', 'Hudson', 'Hull', 'Huntington', 'Hyannis', 'Ipswich', 'Jamaica Plain', 'Lancaster', 'Leicester', 'Lenox', 'Leominster', 'Leverett', 'Lexington', 'Leyden', 'Lowell', 'Lunenburg', 'Lynn', 'Manchester By The Sea', 'Marblehead', 'Marlborough', 'Mashpee', 'Maynard', 'Medfield', 'Medford', 'Medway', 'Methuen', 'Milford', 'Millis', 'Milton', 'Nantucket', 'Needham', 'New Bedford', 'Newton', 'North Adams', 'North Andover', 'North Attleboro', 'Northampton', 'Norton', 'Oak Bluffs', 'Orleans', 'Oxford', 'Peabody', 'Pittsfield', 'Plainfield', 'Plymouth', 'Provincetown', 'Quincy', 'Rehoboth', 'Revere', 'Richmond', 'Rockport', 'Rowley', 'Salem', 'Scituate', 'Shelburne Falls', 'Shrewsbury', 'Somerset', 'Somerville', 'South Dennis', 'Springfield', 'Stockbridge', 'Stoughton', 'Stow', 'Swampscott', 'Swansea', 'Taunton', 'Templeton', 'Tewksbury', 'Uxbridge', 'Vineyard Haven', 'Wakefield', 'Walpole', 'Waltham', 'Watertown', 'Wayland', 'Webster', 'Wellesley', 'Wellfleet', 'West Brookfield', 'West Concord', 'West Stockbridge', 'West Tisbury', 'Williamsburg', 'Williamstown', 'Worcester'))
	state=19
if state=="MD": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Adelphi', 'Annapolis', 'Baltimore', 'Bel Air', 'Berlin', 'Bethesda', 'Bladensburg', 'Bowie', 'Boyds', 'Brunswick', 'Burtonsville', 'California', 'Cambridge', 'Catonsville', 'Clinton', 'College Park', 'Colora', 'Columbia', 'Cumberland', 'Damascus', 'Denton', 'Easton', 'Elkridge', 'Elkton', 'Ellicott City', 'Emmitsburg', 'Essex', 'Forest Hill', 'Frederick', 'Frostburg', 'Gaithersburg', 'Germantown', 'Glen Burnie', 'Greenbelt', 'Hagerstown', 'Havre De Grace', 'Huntingtown', 'Hurlock', 'Hyattsville', 'Jessup', 'Kensington', 'Largo', 'Laurel', 'Leonardtown', 'Mardela Springs', 'Millersville', 'Montgomery Village', 'Mt Airy', 'Newmarket', 'North Bethesda', 'North East', 'Oakland', 'Ocean City', 'Odenton', 'Olney', 'Owings Mills', 'Oxon Hill', 'Pasadena', 'Point Of Rocks', 'Rockville', 'Royal Oak', 'Sabillasville', 'Salisbury', 'Severn', 'Severna Park', 'Silver Spring', 'Stevensville', 'Takoma Park', 'Thurmont', 'Towson', 'Upper Marlboro', 'Waldorf', 'Westminster'))
	state=20
if state=="ME": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alfred', 'Athens', 'Augusta', 'Bailey Island', 'Bangor', 'Bar Harbor', 'Bath', 'Belfast', 'Belmont', 'Biddeford', 'Blue Hill', 'Boothbay', 'Boothbay Harbor', 'Bridgton', 'Brownfield', 'Brunswick', 'Buckfield', 'Bucksport', 'Camden', 'Caribou', 'Carmel', 'Denmark', 'Eliot', 'Ellsworth', 'Falmouth', 'Fort Fairfield', 'Hallowell', 'Houlton', 'Kennebunk', 'Kennebunkport', 'Kittery', 'Lewiston', 'Lincolnville', 'Lisbon Falls', 'Long Island', 'Lowell', 'Machias', 'Maine', 'Milbridge', 'Milo', 'Monhegan', 'Montville', 'Mt Desert', 'Mt Vernon', 'New Sharon', 'Orono', 'Poland', 'Portland', 'Presque Isle', 'Quoddy', 'Rangeley', 'Rockland', 'Rockport', 'Saco', 'Sanford', 'Scarborough', 'Skowhegan', 'South Berwick', 'South Eliot', 'South Portland', 'Steuben', 'Thomaston', 'Turner', 'Union', 'Unity', 'Waldoboro', 'Waterville', 'Wayne', 'Westbrook', 'Winter Harbor', 'Yarmouth', 'York'))
	state=21
if state=="MI": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Adrian', 'Albion', 'Ann Arbor', 'Auburn Hills', 'Battle Creek', 'Bay City', 'Benton Harbor', 'Big Rapids', 'Birmingham', 'Bloomfield Hills', 'Boyne City', 'Brighton', 'Britton', 'Buchanan', 'Byron Center', 'Cadillac', 'Calumet', 'Canton', 'Carleton', 'Caseville', 'Cedar Springs', 'Charlevoix', 'Chelsea', 'Clarkston', 'Climax', 'Crystal Falls', 'Davison', 'Dearborn', 'Dearborn Heights', 'Detroit', 'Dorr', 'Drummond', 'East Jordan', 'East Lansing', 'Elberta', 'Escanaba', 'Farwell', 'Ferndale', 'Flint', 'Goodrich', 'Grand Haven', 'Grand Rapids', 'Grand Rapids Charter Township', 'Greenland', 'Greenville', 'Hamtramck', 'Harbor Springs', 'Harrisville', 'Hartland', 'Hillsdale', 'Holland', 'Hopkins', 'Horton', 'Houghton', 'Howell', 'Huntington Woods', 'Imlay City', 'Indian River', 'Inkster', 'Interlochen', 'Ionia', 'Iron Mountain', 'Iron River', 'Jackson', 'Kalamazoo', 'Kentwood', 'Lake City', 'Lake Orion', 'Lambertville', 'Lansing', 'Lapeer', 'Lee', 'Leonard', 'Livonia', 'Ludington', 'Mackinac Island', 'Macomb', 'Mancelona', 'Marquette', 'Marshall', 'Mesick', 'Michiana', 'Midland', 'Milford', 'Mohawk', 'Monroe', 'Mt Pleasant', 'Muskegon', 'Nashville', 'Newaygo', 'Novi', 'Oak Park', 'Olivet', 'Orion', 'Otsego', 'Owosso', 'Oxford', 'Paw Paw', 'Petoskey', 'Pinckney', 'Plymouth', 'Pontiac', 'Port Huron', 'Ray', 'Redford', 'Rochester', 'Rochester Hills', 'Rockford', 'Romulus', 'Roscommon', 'Royal Oak', 'Saginaw', 'Saranac', 'Shepherd', 'Skandia', 'Southgate', 'Sparta', 'Spring Lake', 'St Clair', 'St Clair Shores', 'St James', 'St Johns', 'St Joseph', 'St Louis', 'Sterling Heights', 'Sturgis', 'Taylor', 'Temperance', 'Traverse', 'Traverse City', 'Troy', 'Utica', 'Vicksburg', 'Village Of Clarkston', 'Waterford', 'Waterford Township', 'West Bloomfield Township', 'West Branch', 'Westland', 'White Lake', 'Whitehall', 'Whitmore Lake', 'Williamston', 'Wixom', 'Wyandotte', 'Wyoming', 'Ypsilanti'))
	state=22
if state=="MN": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Aitkin', 'Annandale', 'Anoka', 'Baudette', 'Baxter', 'Belle Plaine', 'Bemidji', 'Big Lake', 'Bloomington', 'Brainerd', 'Buffalo', 'Burnsville', 'Cass Lake', 'Central', 'Chaska', 'Cottage Grove', 'Crosslake', 'Delano', 'Duluth', 'Eagan', 'Eden Prairie', 'Ely', 'Fairmont', 'Faribault', 'Farmington', 'Forest Lake', 'Glyndon', 'Grand Rapids', 'Green Lake', 'Hopkins', 'Hugo', 'Hutchinson', 'Iron Range', 'Lake Benton', 'Little Canada', 'Luverne', 'Madison', 'Mankato', 'Maplewood', 'Marine On St Croix', 'Medicine Lake', 'Menahga', 'Millville', 'Minneapolis', 'Minnesota Lake', 'Minnetonka', 'Moorhead', 'Morris', 'Northfield', 'Oakdale', 'Owatonna', 'Park Rapids', 'Roseville', 'Saint Cloud', 'Sauk Rapids', 'Savage', 'Shafer', 'Shakopee', 'Shoreview', 'St Cloud', 'St Paul', 'St Peter', 'St. Louis Park', 'Stillwater', 'Two Harbors', 'Vadnais Heights', 'Walnut Grove', 'Waseca', 'Watson', 'Willow River', 'Winona', 'Woodbury'))
	state=23
if state=="MO": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Branson', 'Brentwood', 'Cape Girardeau', 'Chesterfield', 'Columbia', 'Conway', 'Desloge', 'Eagleville', 'Farmington', 'Florissant', 'Fulton', 'Grain Valley', 'Grandview', 'Hannibal', 'Ironton', 'Joplin', 'Kansas City', 'Kirkwood', 'Lake Ozark', 'Lebanon', 'Lexington', 'Macon', 'Maplewood', 'Maysville', 'Neosho', 'Nixa', 'Osage Beach', 'Osceola', 'Owensville', 'Roaring River', 'Scott City', 'Smithville', 'Springfield', 'St Louis', 'St Peters', 'St Robert', 'St. Joseph', 'Thayer', 'Trenton', 'University City', 'Warrensburg', 'Warrenton', 'Webb City', 'West Plains', 'Williamsville', 'Willow Springs'))
	state=24
if state=="MS": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Bay St. Louis', 'Biloxi', 'Blue Springs', 'Brandon', 'Carson', 'Clarksdale', 'Cleveland', 'Clinton', 'Columbus', 'Como', 'Corinth', 'Delta', 'Gulfport', 'Hattiesburg', 'Jackson', 'Meridian', 'Miss State', 'Mound Bayou', 'Ocean Springs', 'Olive Branch', 'Oxford', 'Pearlington', 'Philadelphia', 'Poplarville', 'Port Gibson', 'Ridgeland', 'Starkville', 'Tupelo', 'Yazoo City'))
	state=25
if state=="MT": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Belgrade', 'Big Sandy', 'Big Timber', 'Billings', 'Bozeman', 'Browning', 'Butte', 'Clyde Park', 'Columbia Falls', 'Crow Agency', 'Gallatin Gateway', 'Gardiner', 'Glacier National Park', 'Great Falls', 'Heart Butte', 'Helena', 'Kalispell', 'Lame Deer', 'Livingston', 'Missoula', 'Philipsburg', 'Sidney', 'Stevensville'))
	state=26
if state=="NC": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Apex', 'Asheboro', 'Asheville', 'Atlantic Beach', 'Ayden', 'Banner Elk', 'Beaufort', 'Benson', 'Black Mountain', 'Boone', 'Brevard', 'Bryson City', 'Buies Creek', 'Burlington', 'Burnsville', 'Cameron', 'Carrboro', 'Cary', 'Chapel Hill', 'Charlotte', 'Clayton', 'Climax', 'Como', 'Concord', 'Conover', 'Cullowhee', 'Durham', 'Eden', 'Elk', 'Elkin', 'Elon', 'Elroy', 'Fayetteville', 'Fort Bragg', 'Franklin', 'Fuquay Varina', 'Gastonia', 'Gilkey', 'Graham', 'Greensboro', 'Greenville', 'Hatteras', 'Havelock', 'Hendersonville', 'Hertford', 'Hickory', 'High Point', 'Highlands', 'Hillsborough', 'Huntersville', 'Jacksonville', 'Jamestown', 'Kannapolis', 'Kernersville', 'King', 'Kinston', 'Lexington', 'Linden', 'Lumberton', 'Marion', 'Mars Hill', 'Marshall', 'Matthews', 'Mebane', 'Mint Hill', 'Mocksville', 'Monroe', 'Mooresville', 'Morganton', 'Morrisville', 'New Bern', 'New Hope', 'Newton', 'Old Fort', 'Oxford', 'Pilot Mountain', 'Pittsboro', 'Pleasant Garden', 'Raleigh', 'Richlands', 'Rocky Mt', 'Rutherfordton', 'Salisbury', 'Saluda', 'Sanford', 'Saxapahaw', 'Seagrove', 'Shelby', 'Siler City', 'Southern Pines', 'Southern Shores', 'Southport', 'Statesville', 'Sylva', 'Thomasville', 'Topsail', 'Triangle', 'West End', 'Westfield', 'Whitsett', 'Wilkesboro', 'Wilmington', 'Winston Salem', 'Zirconia'))
	state=27
if state=="ND": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Bismarck', 'Fargo', 'Grand Forks', 'Hettinger', 'Kensal', 'Minot', 'Neche', 'New Leipzig', 'New Town', 'Williston'))
	state=28
if state=="NE": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Bayard', 'Blue Hill', 'Bruning', 'Clarkson', 'Cozad', 'Elkhorn', 'Gering', 'Grand Island', 'Kearney', 'Kenesaw', 'Lincoln', 'Minden', 'North Platte', 'Omaha', 'Palmyra', 'Santee', 'Scottsbluff', 'Sidney', 'Sutton', 'York'))
	state=29
if state=="NH": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alstead', 'Amherst', 'Antrim', 'Barrington', 'Bedford', 'Bethlehem', 'Claremont', 'Concord', 'Derry', 'Dover', 'Durham', 'East Wakefield', 'Effingham', 'Exeter', 'Farmington', 'Fitzwilliam', 'Gilmanton Iw', 'Hampstead', 'Hampton', 'Hanover', 'Henniker', 'Hinsdale', 'Hollis', 'Keene', 'Lancaster', 'Londonderry', 'Lyme', 'Manchester', 'Meredith', 'Merrimack', 'Nashua', 'New Hampton', 'New London', 'Newmarket', 'Northwood', 'Peterborough', 'Plymouth', 'Portsmouth', 'Raymond', 'Rochester', 'Rollinsford', 'Salem', 'Somersworth', 'Sutton', 'Thornton', 'Tilton', 'Warren', 'Weare', 'Winchester'))
	state=30
if state=="NJ": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Absecon', 'Allentown', 'Andover', 'Asbury Park', 'Atlantic City', 'Avenel', 'Barnegat', 'Barrington', 'Bayonne', 'Beach Haven West', 'Belleville', 'Belmar', 'Bergenfield', 'Berkeley', 'Bloomfield', 'Bogota', 'Boonton', 'Bordentown', 'Branchburg', 'Brick', 'Brick Township', 'Bridgewater', 'Bridgewater Township', 'Burlington', 'Butler', 'Byram', 'Caldwell', 'Camden', 'Cape May', 'Carteret', 'Chatsworth', 'Cherry Hill', 'Clarksboro', 'Clifton', 'Clinton', 'Collingswood', 'Colonia', 'Cranbury', 'Cranford', 'Cresskill', 'Delran', 'Denville', 'Dumont', 'East Brunswick', 'East Hanover', 'East Orange', 'Eastampton', 'Edison', 'Egg Harbor Township', 'Elizabeth', 'Emerson', 'Englewood', 'Englewood Cliffs', 'Ewing', 'Fair Lawn', 'Fanwood', 'Farmingdale', 'Flanders', 'Flemington', 'Florham Park', 'Fort Dix', 'Fort Lee', 'Franklin Lakes', 'Franklin Park', 'Freehold', 'Frenchtown', 'Glassboro', 'Gloucester City', 'Green Brook', 'Hackensack', 'Hackettstown', 'Haddon Heights', 'Haddonfield', 'Haledon', 'Hamburg', 'Hamilton', 'Hamilton Township', 'Hammonton', 'Hardyston', 'Harrison', 'Hawthorne', 'Hewitt', 'Highland Park', 'Hightstown', 'Hillsdale', 'Hillside', 'Hoboken', 'Holmdel Township', 'Hopatcong', 'Jackson', 'Jersey City', 'Kearny', 'Keyport', 'Kinnelon', 'Lake Hopatcong', 'Laurence Harbor', 'Layton', 'Leonia', 'Linden', 'Lindenwold', 'Little Egg Harbor', 'Long Branch', 'Loveladies', 'Madison', 'Mahwah', 'Manahawkin', 'Manalapan', 'Manasquan', 'Maplewood', 'Marlboro', 'Marlton', 'Matawan', 'Mays Landing', 'Maywood', 'Mendham', 'Mendham Township', 'Metuchen', 'Middlesex', 'Middletown', 'Millville', 'Monroe Township', 'Montclair', 'Montville', 'Moorestown', 'Morristown', 'Mt Holly', 'Mullica Hill', 'National Park', 'Neptune City', 'Netcong', 'New Brunswick', 'New Providence', 'Newark', 'Newfield', 'Newton', 'North Bergen', 'North Brunswick Township', 'North Hanover', 'North Wildwood', 'Northfield', 'Norwood', 'Nutley', 'Oakhurst', 'Oakland', 'Oaklyn', 'Ocean Grove', 'Old Bridge', 'Paramus', 'Parsippany', 'Paterson', 'Paulsboro', 'Pennington', 'Pennsauken', 'Phillipsburg', 'Piscataway', 'Plainfield', 'Plainsboro', 'Point Pleasant', 'Point Pleasant Beach', 'Port Norris', 'Princeton', 'Rahway', 'Randolph', 'Red Bank', 'Ridgewood', 'Ringwood', 'River Vale', 'Robbinsville', 'Rockaway', 'Rumson', 'Rutherford', 'Sayreville', 'Scotch Plains', 'Secaucus', 'Sewaren', 'Ship Bottom', 'Short Hills', 'Sicklerville', 'Somers Point', 'Somerset', 'South Bound Brook', 'South Orange', 'Sparta', 'Spotswood', 'Spring Lake', 'Springfield', 'Stratford', 'Succasunna', 'Summit', 'Sussex', 'Teaneck', 'Tenafly', 'Tewksbury', 'Toms River', 'Totowa', 'Trenton', 'Union', 'Union City', 'Upper Freehold', 'Upper Pittsgrove', 'Ventnor City', 'Vernon', 'Vineland', 'Wall Township', 'Washington', 'Wayne', 'Weehawken', 'West Deptford Township', 'West Long Branch', 'West Orange', 'Westwood', 'Whitehouse Station', 'Wildwood', 'Willingboro', 'Winslow', 'Woodbury', 'Woodbury Heights'))
	state=31
if state=="NM": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Albuquerque', 'Alcalde', 'Artesia', 'Aztec', 'Cerrillos', 'Clovis', 'Cochiti Lake', 'Desert', 'El Morro', 'Espanola', 'Farmington', 'Galisteo', 'Gallup', 'La Luz', 'Las Cruces', 'Las Vegas', 'Los Alamos', 'Luna', 'Madrid', 'Mora', 'Paguate', 'Portales', 'Questa', 'Rio Rancho', 'Roswell', 'Ruidoso', 'Santa Fe', 'Shiprock', 'Socorro', 'Taos', 'Tijeras', 'Truth Or Consequences'))
	state=32
if state=="NV": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Battle Mountain', 'Boulder City', 'Carson City', 'Dayton', 'Fallon', 'Gardnerville', 'Gerlach Empire', 'Henderson', 'Imlay', 'Las Vegas', 'Minden', 'North Las Vegas', 'Reno', 'Sparks', 'Stateline', 'Tonopah'))
	state=33
if state=="NY": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Adirondack', 'Albany', 'Albion', 'Alexandria Bay', 'Alfred', 'Angola', 'Annandale On Hudson', 'Astoria', 'Auburn', 'Averill Park', 'Avon', 'Babylon', 'Baldwinsville', 'Ballston Spa', 'Barrytown', 'Bay Shore', 'Bayport', 'Beacon', 'Bedford   Stuyvesant', 'Bellmore', 'Bethpage', 'Binghamton', 'Bohemia', 'Brentwood', 'Brewster', 'Bridgehampton', 'Bronx', 'Bronxville', 'Brooklyn', 'Buffalo', 'Bushwick', 'Canaan', 'Canandaigua', 'Candor', 'Canton', 'Catskill', 'Cazenovia', 'Centerport', 'Chappaqua', 'Chatham', 'Cherry Valley', 'Chittenango', 'Clinton Corners', 'Cold Brook', 'Cold Spring', 'Colonie', 'Coney Island', 'Corning', 'Cornwall', 'Cortlandt Manor', 'Cragsmoor', 'Croton On Hudson', 'Crown Heights', 'Cutchogue', 'Delancey', 'Delhi', 'Dix Hills', 'Durham', 'East Aurora', 'East Greenbush', 'East Hampton', 'East Harlem', 'East Meadow', 'East Northport', 'East Village', 'Ellenville', 'Elmhurst', 'Endicott', 'Esopus', 'Far Rockaway', 'Farmingdale', 'Ferndale', 'Fishkill', 'Florida', 'Flushing', 'Forest Hills', 'Franklin Square', 'Fredonia', 'Freeport', 'Geneseo', 'Geneva', 'Ghent', 'Gilgo Oak Beach Captree', 'Glen Cove', 'Glens Falls', 'Goldens Bridge', 'Goshen', 'Grand Island', 'Great Neck', 'Greenlawn', 'Greenpoint', 'Greenport', 'Greenwich', 'Greenwood Lake', 'Hamilton', 'Hammondsport', 'Hancock', 'Harlem', 'Hastings On Hudson', 'Haverstraw', 'Hawthorne', 'Hector', 'Hempstead', 'Herkimer', 'Hicksville', 'High Falls', 'Highland', 'Highland Mills', 'Hoboken', 'Holland', 'Holtsville', 'Honeoye Falls', 'Hopewell Junction', 'Horseheads', 'Hudson', 'Hunter', 'Huntington', 'Huntington Station', 'Hyde Park', 'Ilion', 'Inlet', 'Islip', 'Ithaca', 'Jay', 'Jersey City', 'Kinderhook', 'Kingston', 'Kirkville', 'Lake George', 'Lake Placid', 'Levittown', 'Lewiston', 'Lindenhurst', 'Liverpool', 'Long Beach', 'Long Island', 'Long Island City', 'Lower East Side', 'Lynbrook', 'Macedon', 'Mahopac', 'Mamaroneck', 'Manhattan', 'Marbletown', 'Marcellus', 'Margaretville', 'Marion', 'Massapequa', 'Mastic', 'Mastic Beach', 'Middletown', 'Millerton', 'Mohawk', 'Monroe', 'Monsey', 'Montauk', 'Montgomery', 'Montrose', 'Mount Vernon', 'Mt Vernon', 'Munnsville', 'Nanuet', 'New', 'New City', 'New Paltz', 'New Rochelle', 'New York', 'Newburgh', 'Niagara Falls', 'Niskayuna', 'North Creek', 'Northport', 'Nyack', 'Oneonta', 'Ossining', 'Oswego', 'Oyster Bay', 'Palenville', 'Parish', 'Park Slope', 'Patchogue', 'Pearl River', 'Peekskill', 'Philadelphia', 'Piermont', 'Pine Plains', 'Plattsburgh', 'Pleasant Valley', 'Pleasantville', 'Port Chester', 'Port Ewen', 'Port Jefferson', 'Potsdam', 'Poughkeepsie', 'Pound Ridge', 'Purchase', 'Queens', 'Queensbury', 'Red Hook', 'Redwood', 'Ridge', 'Ridgewood', 'Rochester', 'Rockland', 'Rockville Centre', 'Rocky Point', 'Rome', 'Ronkonkoma', 'Rosendale', 'Rotterdam', 'Sag Harbor', 'Saint James', 'Salamanca', 'Salem', 'Saranac Lake', 'Saratoga Springs', 'Saugerties', 'Sayville', 'Scarsdale', 'Schenectady', 'Scotia', 'Seaford', 'Shandaken', 'Shelter Island', 'Sidney', 'Smithtown', 'Soho', 'Somers', 'South Salem', 'Southampton', 'Southold', 'Spring Valley', 'Staten Island', 'Stillwater', 'Stone Ridge', 'Stony Brook', 'Stony Point', 'Suffern', 'Sunnyside', 'Sylvan Beach', 'Syracuse', 'Tarrytown', 'Thurston', 'Tivoli', 'Tomkins Cove', 'Troy', 'Truxton', 'Tuckahoe', 'Ulysses', 'Utica', 'Valley Cottage', 'Vestal', 'Wainscott', 'Walden', 'Walworth', 'Wappingers Falls', 'Warsaw', 'Warwick', 'Washington Heights', 'Washingtonville', 'Wassaic', 'Watertown', 'Watkins Glen', 'Wawayanda', 'Wayland', 'West Babylon', 'West Fulton', 'West Hempstead', 'Westhampton Beach', 'Westport', 'White Plains', 'Williamsburg', 'Willsboro', 'Windsor', 'Woodmere', 'Woodstock', 'Wynantskill', 'Yonkers', 'Yorktown Heights'))
	state=34
if state=="OH": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Akron', 'Ashland', 'Ashtabula', 'Athens', 'Bainbridge', 'Batavia', 'Bellefontaine', 'Bellville', 'Bluffton', 'Bowling Green', 'Brookville', 'Butler Township', 'Cadiz', 'Canal Fulton', 'Canal Winchester', 'Canton', 'Cardington', 'Cedarville', 'Centerville', 'Chagrin Falls', 'Chesterhill', 'Cincinnati', 'Clayton', 'Cleveland', 'Cleveland Heights', 'Columbus', 'Concord', 'Conneaut', 'Continental', 'Cuyahoga Falls', 'Dalton', 'Dayton', 'Defiance', 'Delaware', 'Eastlake', 'Edon', 'Elmore', 'Elyria', 'Euclid', 'Fairborn', 'Findlay', 'Gallipolis', 'Granville', 'Green', 'Hamilton', 'Hebron', 'Hilliard', 'Holgate', 'Huber Heights', 'Hudson', 'Kent', 'Kettering', 'Lakewood', 'Lebanon', 'Lorain', 'Madeira', 'Maineville', 'Mansfield', 'Mantua', 'Marietta', 'Marion', 'Martins Ferry', 'Mason', 'Massillon', 'Mentor', 'Middlefield', 'Middleport', 'Middletown', 'Monroe', 'Moraine', 'Mt Gilead', 'Napoleon', 'New Concord', 'New Lexington', 'New Philadelphia', 'Newark', 'North Canton', 'North Lewisburg', 'North Royalton', 'Northwood', 'Norwood', 'Oberlin', 'Ohio City', 'Oregon', 'Orrville', 'Oxford', 'Parma', 'Port Clinton', 'Quaker City', 'Richfield', 'Richwood', 'Rutland', 'Sandusky', 'Seville', 'Shaker Heights', 'Sidney', 'South Amherst', 'Springfield', 'Stow', 'Thompson', 'Toledo', 'Toronto', 'Troy', 'Urbana', 'Wadsworth', 'Warren', 'Washington Court House', 'Waynesburg', 'Wellsville', 'West Chester', 'Westerville', 'Whitehouse', 'Wilmington', 'Wooster', 'Yellow Springs', 'Youngstown', 'Zanesville'))
	state=35
if state=="OK": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Ada', 'Bartlesville', 'Bristow', 'Broken Arrow', 'Durant', 'Edmond', 'El Reno', 'Fort Sill', 'Guymon', 'Lawton', 'Lindsay', 'Mannford', 'Midwest City', 'Muskogee', 'Mustang', 'Mutual', 'Noble', 'Norman', 'Oklahoma City', 'Sallisaw', 'Seminole', 'Shawnee', 'Stillwater', 'Stroud', 'Sulphur', 'Tahlequah', 'Tulsa', 'Wagoner', 'Weatherford'))
	state=36
if state=="OR": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Albany', 'Amity', 'Ashland', 'Astoria', 'Bandon', 'Banks', 'Beaverton', 'Bend', 'Brownsville', 'Canby', 'Central Point', 'Coos Bay', 'Corvallis', 'Cottage Grove', 'Crescent Lake', 'Damascus', 'Elkton', 'Enterprise', 'Eugene', 'Forest Grove', 'Gold Beach', 'Grants Pass', 'Gresham', 'Hermiston', 'Hillsboro', 'Hood River', 'Jacksonville', 'Klamath Falls', 'La Grande', 'Lake Oswego', 'Lebanon', 'Mc Minnville', 'Medford', 'Milwaukie', 'Molalla', 'Myrtle Creek', 'Neskowin', 'Newberg', 'Newport', 'North Bend', 'Northwest Josephine', 'Nyssa', 'Oregon City', 'Otis', 'Pacific City', 'Phoenix', 'Port Orford', 'Portland', 'Reedsport', 'Roseburg', 'Salem', 'Sandy', 'Seaside', 'Sherwood', 'Silverton', 'Sisters', 'Springfield', 'Talent', 'The Dalles', 'Tigard', 'Tillamook', 'Tualatin', 'Union', 'Warren', 'Williams', 'Wilsonville', 'Woodburn', 'Yachats'))
	state=37
if state=="PA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Allentown', 'Altoona', 'Ambler', 'Amity', 'Ardmore', 'Bally', 'Beaver Falls', 'Bensalem', 'Bethlehem', 'Blooming Grove', 'Bloomsburg', 'Boalsburg', 'Boiling Springs', 'Braddock', 'Bradford', 'Bryn Mawr', 'Butler', 'Camp Hill', 'Carbondale', 'Carlisle', 'Carmichaels', 'Centralia', 'Chadds Ford', 'Chalfont', 'Chambersburg', 'Cheltenham', 'Chester Springs', 'Cheswick', 'Clarion', 'Coatesville', 'Collegeville', 'Coudersport', 'Danville', 'Delaware Water Gap', 'Dillsburg', 'Dormont', 'Downingtown', 'Doylestown', 'Dunmore', 'East Stroudsburg', 'Easton', 'Edinboro', 'Elizabethtown', 'Elverson', 'Erie', 'Etters', 'Everett', 'Exton', 'Factoryville', 'Fleetwood', 'Germany', 'Gettysburg', 'Glen Rock', 'Glenolden', 'Glenside', 'Greencastle', 'Greensburg', 'Grove City', 'Halifax', 'Hamburg', 'Hamilton', 'Harleysville', 'Harrisburg', 'Hatboro', 'Hawley', 'Hazleton', 'Hellam', 'Hermitage', 'Hershey', 'Hookstown', 'Howard', 'Hummelstown', 'Indiana', 'Ivyland', 'Jim Thorpe', 'Johnstown', 'Kane', 'King Of Prussia', 'Kutztown', 'Lake City', 'Lancaster', 'Landenberg', 'Langhorne', 'Lansdale', 'Latrobe', 'Lebanon', 'Lewisburg', 'Lewistown', 'Ligonier', 'Lumberville', 'Luzerne', 'Macungie', 'Maple Glen', 'Mars', 'Marysville', 'Mc Keesport', 'Meadville', 'Mechanicsburg', 'Media', 'Middletown', 'Mt Joy', 'Muncy', 'Nanticoke', 'New Castle', 'New Cumberland', 'New Hope', 'New Oxford', 'New Wilmington', 'Newport', 'Newtown', 'Newtown Square', 'North Versailles', 'Northampton', 'Oliver', 'Oxford', 'Pen Argyl', 'Penndel', 'Perkasie', 'Philadelphia', 'Phoenixville', 'Pittsburgh', 'Pittston', 'Plainfield', 'Pocono', 'Pottsville', 'Quakertown', 'Reading', 'Riegelsville', 'Rockledge', 'Roseto', 'Royersford', 'Saltsburg', 'Schwenksville', 'Scranton', 'Shade Gap', 'Shenandoah', 'Shippensburg', 'Slippery Rock', 'South Woodbury', 'Southampton', 'State College', 'Stewartstown', 'Stillwater', 'Stroudsburg', 'Turtle Creek', 'Vanderbilt', 'Waynesboro', 'Wernersville', 'West Chester', 'West Grove', 'Wilkes Barre', 'Williamsport', 'Willow Grove', 'Yardley', 'York'))
	state=38
if state=="RI": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Barrington', 'Bristol', 'Cranston', 'Cumberland', 'East Greenwich', 'East Providence', 'Exeter', 'Foster', 'Johnston', 'Kingston', 'Lincoln', 'Narragansett', 'Newport', 'North Kingstown', 'North Providence', 'North Smithfield', 'Pawtucket', 'Providence', 'Rumford', 'Scituate', 'Smithfield', 'South Kingstown', 'Wakefield Peacedale', 'Warwick', 'West Warwick', 'Woonsocket'))
	state=39
if state=="SC": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Aiken', 'Anderson', 'Back Swamp', 'Beaufort', 'Belton', 'Bluffton', 'Boiling Springs', 'Camden', 'Charleston', 'Cheraw', 'Cleland Crossroads', 'Clemson', 'Columbia', 'Conway', 'Dalzell', 'Dorchester', 'Easley', 'Edgefield', 'Florence', 'Folly Beach', 'Fort Mill', 'Gaston', 'Greenville', 'Greenwood', 'Hilton Head Island', 'Lake City', 'Lancaster', 'Lexington', 'Little River', 'Manning', 'Moncks Corner', 'Mount Pleasant', 'Myrtle Beach', 'Newberry', 'North', 'North Augusta', 'North Charleston', 'North Myrtle Beach', 'Orangeburg', 'Pickens', 'Ridge Spring', 'Rock Hill', 'Seneca', 'Simpsonville', 'Spartanburg', 'Summerville', 'Sumter', 'Travelers Rest', 'Walhalla', 'Wellford', 'West Columbia'))
	state=40
if state=="SD": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Aberdeen', 'Beresford', 'Brandon', 'Brookings', 'Bullhead', 'Custer', 'Eagle Butte', 'Faulkton', 'Gayville', 'Harrisburg', 'Hill City', 'Hot Springs', 'Interior', 'Lead', 'Lower Brule', 'Madison', 'Mission', 'Mitchell', 'Oneota', 'Pierre', 'Pine Ridge', 'Rapid City', 'Sioux Falls', 'Southwest Meade', 'West Shannon', 'Yankton'))
	state=41
if state=="TN": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Bell Buckle', 'Bethel Springs', 'Blaine', 'Bluff City', 'Bristol', 'Chattanooga', 'Clarksville', 'Cleveland', 'Clinton', 'Collegedale', 'Columbia', 'Cookeville', 'Covington', 'Dayton', 'Dover', 'East Nashville', 'Elizabethton', 'Erwin', 'Fairview', 'Franklin', 'Gatlinburg', 'Greenbrier', 'Greeneville', 'Hendersonville', 'Jackson', 'Jefferson City', 'Johnson City', 'Jonesborough', 'Kingsport', 'Knoxville', 'Lexington', 'Manchester', 'Martin', 'Maryville', 'Memphis', 'Morristown', 'Mt Juliet', 'Murfreesboro', 'Nashville', 'Nashville Davidson (Balance)', 'Newport', 'Oak Ridge', 'Pigeon Forge', 'Portland', 'Selmer', 'Smyrna', 'Springfield', 'Summertown', 'Wartburg', 'Westmoreland', 'White House'))
	state=42
if state=="TX": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Abilene', 'Ackerly', 'Addison', 'Allen', 'Amarillo', 'Arlington', 'Austin', 'Avery', 'Bandera', 'Beaumont', 'Beckville', 'Bedford', 'Bellaire', 'Blanco', 'Boerne', 'Brownsville', 'Bryan', 'Buda', 'Buna', 'Burleson', 'Cameron', 'Canyon', 'Canyon Lake', 'Carrollton', 'Cedar Park', 'Central', 'Channing', 'Childress', 'China Grove', 'Christoval', 'Coldspring', 'College Station', 'Comfort', 'Corinth', 'Corpus Christi', 'Corsicana', 'Cross Plains', 'Crystal City', 'Dallas', 'Decatur', 'Del Rio', 'Dell City', 'Denison', 'Denton', 'Dickinson', 'Dublin', 'Earth', 'East', 'Edinburg', 'El Paso', 'Euless', 'Fairfield', 'Ferris', 'Floresville', 'Flower Mound', 'Forney', 'Fort Bliss', 'Fort Worth', 'Friona', 'Frisco', 'Fulshear', 'Gainesville', 'Galveston', 'Garland', 'Georgetown', 'Grand Prairie', 'Grapevine', 'Greenville', 'Gun Barrel City', 'Hallettsville', 'Harlingen San Benito', 'Henderson', 'High Island', 'Houston', 'Huntsville', 'Hurst', 'Irving', 'Italy', 'Katy', 'Kilgore', 'Killeen', 'Kingsbury', 'Kyle', 'Lago Vista', 'Lake Jackson', 'Laredo', 'League City', 'Leander', 'Lewisville', 'Llano', 'Longview', 'Lubbock', 'Lufkin', 'Marfa', 'Marlin', 'Mc Allen', 'Mc Kinney', 'Melissa', 'Meridian', 'Mesquite', 'Midland', 'Mission', 'Nacogdoches', 'Nederland', 'New Braunfels', 'Odessa', 'Palestine', 'Panhandle', 'Paris', 'Pearland', 'Pecos', 'Pilot Point', 'Plano', 'Ponder', 'Port Arthur', 'Quitman', 'Rockport', 'Round Rock', 'Rowlett', 'Sachse', 'Samnorwood', 'San Angelo', 'San Antonio', 'San Marcos', 'Seabrook', 'Shenandoah', 'Sierra Blanca', 'Smithville', 'Southwest', 'Spring', 'Springtown', 'Sugar Land', 'Sulphur Springs', 'Temple', 'Terlingua', 'Texarkana', 'The Colony', 'The Woodlands', 'Tomball', 'Tyler', 'University Park', 'Van Alstyne', 'Waco', 'Waller', 'Waxahachie', 'Weatherford', 'West', 'Weston', 'Wills Point', 'Wimberley'))
	state=43
if state=="UT": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'American Fork', 'Blanding', 'Bountiful', 'Brigham City', 'Cedar City', 'Cedar Hills', 'Centerville', 'Draper', 'Eagle Mountain', 'Ephraim', 'Green River', 'Heber', 'Honeyville', 'Hurricane', 'Kanab', 'Kaysville', 'Layton', 'Lehi', 'Logan', 'Mapleton', 'Midway', 'Moab', 'Ogden', 'Orem', 'Park City', 'Payson', 'Pleasant Grove', 'Pleasant View', 'Providence', 'Provo', 'Riverton', 'Salem', 'Salt Lake City', 'Sandy', 'Saratoga Springs', 'Smithfield', 'South Jordan', 'Spanish Fork', 'Springville', 'St George', 'Syracuse', 'Tooele', 'West Jordan'))
	state=44
if state=="VA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Alexandria', 'Amherst', 'Annandale', 'Ararat', 'Arlington', 'Arrington', 'Ashburn', 'Beaverdam', 'Berryville', 'Big Stone Gap', 'Blacksburg', 'Blue Ridge', 'Bridgewater', 'Bristol', 'Bristow', 'Buckingham', 'Charlottesville', 'Chesapeake', 'Chesterfield', 'Colonial Beach', 'Culpeper', 'Dahlgren', 'Danville', 'Dublin', 'Emporia', 'Fairfax', 'Falls Church', 'Farmville', 'Floyd', 'Forest', 'Fork Union', 'Fredericksburg', 'Front Royal', 'Gainesville', 'Glen Allen', 'Gloucester', 'Hampton', 'Harrisonburg', 'Herndon', 'Ivanhoe', 'Leesburg', 'Lorton', 'Luray', 'Lynchburg', 'Manassas', 'Marion', 'Martinsville', 'Mechanicsville', 'Midlothian', 'Mineral', 'Montpelier', 'Newport News', 'Norfolk', 'North Springfield', 'Northern', 'Oakton', 'Parksley', 'Peaks', 'Portsmouth', 'Powhatan', 'Pulaski', 'Purcellville', 'Quantico', 'Radford', 'Red Oak', 'Richmond', 'Roanoke', 'South Boston', 'South Hill', 'Springfield', 'Stafford', 'Staunton', 'Sterling', 'Suffolk', 'Taylorstown', 'Tazewell', 'Verona', 'Vienna', 'Virgilina', 'Virginia Beach', 'Wakefield', 'Washington', 'Waynesboro', 'Williamsburg', 'Winchester', 'Wise', 'Woodbridge', 'Woodstock', 'Yorktown'))
	state=45
if state=="VT": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Barnard', 'Barre', 'Barton', 'Bellows Falls', 'Bennington', 'Brandon', 'Brattleboro', 'Bristol', 'Brookfield', 'Brookline', 'Burlington', 'Calais', 'Castleton', 'Chittenden', 'Elmore', 'Enosburg Falls', 'Essex Junction', 'Fairlee', 'Franklin', 'Hardwick', 'Hinesburg', 'Hyde Park', 'Johnson', 'Lincoln', 'Ludlow', 'Manchester', 'Middlebury', 'Milton', 'Montpelier', 'Morrisville', 'Newbury', 'Newfane', 'Norwich', 'Poultney', 'Putney', 'Randolph', 'Richmond', 'Roxbury', 'Rutland', 'Sharon', 'Sheffield', 'Shelburne', 'Shoreham', 'St Johnsbury', 'Starksboro', 'Stockbridge', 'Stowe', 'Sunderland', 'Taftsville', 'Tinmouth', 'Townshend', 'Tunbridge', 'Vergennes', 'Waitsfield', 'Wells', 'West Dover', 'West Topsham', 'Westminster', 'White River Junction', 'Williston', 'Windsor', 'Woodstock'))
	state=46
if state=="WA": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Aberdeen', 'Anacortes', 'Arlington', 'Auburn', 'Bainbridge Island', 'Bellevue', 'Bellingham', 'Birch Bay', 'Blaine', 'Bonney Lake', 'Bothell', 'Bremerton', 'Buckley', 'Burbank', 'Burien', 'Camano Island', 'Camas', 'Carlton', 'Centralia', 'Chehalis', 'Cheney', 'Clinton', 'Colfax', 'Coupeville', 'Desert Aire', 'Duvall', 'Edmonds', 'Ellensburg', 'Enumclaw', 'Everett', 'Forks', 'Fort Lewis', 'Frederickson', 'Freeland', 'Friday Harbor', 'George', 'Gig Harbor', 'Hoquiam', 'Indianola', 'Issaquah', 'Kelso', 'Kenmore', 'Kennewick', 'Kent', 'Kettle Falls', 'Kingston', 'Kirkland', 'Lacey', 'Leavenworth', 'Longview', 'Lopez Island', 'Lynden', 'Lynnwood', 'Mabton', 'Marysville', 'Mercer Island', 'Mill Creek', 'Monroe', 'Montesano', 'Moses Lake', 'Mountlake Terrace', 'Mt Vernon', 'Neah Bay', 'Oak Harbor', 'Olalla', 'Olympia', 'Orcas', 'Pasco', 'Port Angeles', 'Port Orchard', 'Port Townsend', 'Poulsbo', 'Pullman', 'Puyallup', 'Quilcene', 'Redmond', 'Renton', 'Richland', 'Ridgefield', 'Roslyn', 'Sammamish', 'Seattle', 'Sequim', 'Shelton', 'Shoreline', 'Snohomish', 'Spokane', 'Spokane Valley', 'Sprague', 'Stanwood', 'Stehekin', 'Steilacoom', 'Sultan', 'Sumner', 'Suquamish', 'Tacoma', 'Tieton', 'Twisp', 'Vancouver', 'Vashon', 'Walla Walla', 'Wenatchee', 'White Salmon', 'White Swan', 'Wilbur', 'Woodland', 'Yakima', 'Yelm'))
	state=47
if state=="WI": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Amery', 'Appleton', 'Baraboo', 'Bayfield', 'Beaver Dam', 'Beloit', 'Brodhead', 'Brown Deer', 'Chippewa Falls', 'Clayton', 'De Forest', 'De Pere', 'Delavan', 'Dodgeville', 'Eau Claire', 'Edgerton', 'Elm Grove', 'Fish Creek', 'Fremont', 'Green Bay', 'Hartford', 'Hubertus', 'Jacksonport', 'Kaukauna', 'Kenosha', 'La Pointe', 'Lake Geneva', 'Madison', 'Manitowoc', 'Mazomanie', 'Menasha', 'Menomonie', 'Mequon', 'Merrill', 'Milwaukee', 'Mukwonago', 'Neenah', 'Nelson', 'New Richmond', 'Oak Creek', 'Oconomowoc', 'Oregon', 'Osceola', 'Oshkosh', 'Oulu', 'Pepin', 'Plymouth', 'Racine', 'Randolph', 'Rhinelander', 'Rice Lake', 'River Falls', 'Sauk City', 'Saukville', 'Sharon', 'Sheboygan Falls', 'Shell Lake', 'Sparta', 'Steuben', 'Stevens Point', 'Sturgeon Bay', 'Sun Prairie', 'Superior', 'Tomah', 'Union Grove', 'Viroqua', 'Washburn', 'Washington Island', 'Waukesha', 'Waunakee', 'Wausau', 'Wauwatosa', 'West Bend', 'Westby', 'Whitewater', 'Wisconsin Dells'))
	state=48
if state=="WV": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Athens', 'Barboursville', 'Beaver', 'Buckhannon', 'Cass', 'Charleston', 'Clarksburg', 'Elkins', 'Fairmont', 'Falling Waters', 'Granville', 'Harpers Ferry', 'Hillsboro', 'Huntington', 'Hurricane', 'Inwood', 'Jane Lew', 'Jolo', 'Lewisburg', 'Madison', 'Martinsburg', 'Meadow Bridge', 'Morgantown', 'Northern', 'Parkersburg', 'Ripley', 'Southern', 'Spencer', 'St Albans', 'Wheeling'))
	state=49
if state=="WY": 
	city = st.sidebar.selectbox( 'Select the city for your project?', ('Select City', 'Buffalo', 'Casper', 'Cheyenne', 'Cody', 'Dubois', 'Gillette', 'Jackson', 'Laramie', 'Midwest', 'Newcastle', 'Powder River'))
	state=50

goal = st.sidebar.text_input("Enter goal for the project? (without commas)", 0)
updates = st.sidebar.text_input("Enter total number of updates for the project?", 0)
duration = st.sidebar.text_input("Enter duration of the project? (in days)", 0)
level = st.sidebar.text_input("Enter Number of Levels? (Max 15):", 0)
name = st.sidebar.text_input("Enter your Full Name:")
email = st.sidebar.text_input("Enter your Email ID")

if sub_cat=="Animation": sub_cat=0
if sub_cat=="Art": sub_cat=1
if sub_cat=="Art Book": sub_cat=2
if sub_cat=="Board & Card Games": sub_cat=3
if sub_cat=="Board &amp; Card Games": sub_cat=4
if sub_cat=="Children's Book": sub_cat=5
if sub_cat=="Classical Music": sub_cat=6
if sub_cat=="Comics": sub_cat=7
if sub_cat=="Conceptual Art": sub_cat=8
if sub_cat=="Country & Folk": sub_cat=9
if sub_cat=="Country &amp; Folk": sub_cat=10
if sub_cat=="Crafts": sub_cat=11
if sub_cat=="Dance": sub_cat=12
if sub_cat=="Design": sub_cat=13
if sub_cat=="Digital Art": sub_cat=14
if sub_cat=="Documentary": sub_cat=15
if sub_cat=="Electronic Music": sub_cat=16
if sub_cat=="Fashion": sub_cat=17
if sub_cat=="Fiction": sub_cat=18
if sub_cat=="Film &amp; Video": sub_cat=19
if sub_cat=="Food": sub_cat=20
if sub_cat=="Games": sub_cat=21
if sub_cat=="Graphic Design": sub_cat=22
if sub_cat=="Hip-Hop": sub_cat=23
if sub_cat=="Illustration": sub_cat=24
if sub_cat=="Indie Rock": sub_cat=25
if sub_cat=="Jazz": sub_cat=26
if sub_cat=="Journalism": sub_cat=27
if sub_cat=="Mixed Media": sub_cat=28
if sub_cat=="Music": sub_cat=29
if sub_cat=="Narrative Film": sub_cat=30
if sub_cat=="Nonfiction": sub_cat=31
if sub_cat=="Open Hardware": sub_cat=32
if sub_cat=="Open Software": sub_cat=33
if sub_cat=="Painting": sub_cat=34
if sub_cat=="Performance Art": sub_cat=35
if sub_cat=="Periodical": sub_cat=36
if sub_cat=="Photography": sub_cat=37
if sub_cat=="Poetry": sub_cat=38
if sub_cat=="Pop": sub_cat=39
if sub_cat=="Product Design": sub_cat=40
if sub_cat=="Public Art": sub_cat=41
if sub_cat=="Publishing": sub_cat=42
if sub_cat=="Rock": sub_cat=43
if sub_cat=="Sculpture": sub_cat=44
if sub_cat=="Short Film": sub_cat=45
if sub_cat=="Technology": sub_cat=46
if sub_cat=="Theater": sub_cat=47
if sub_cat=="Video Games": sub_cat=48
if sub_cat=="Webseries": sub_cat=49
if sub_cat=="World Music": sub_cat=50

if city=="1": city=0
if city=="Aberdeen": city=1
if city=="Abilene": city=2
if city=="Absecon": city=3
if city=="Ackerly": city=4
if city=="Ackworth": city=5
if city=="Acton": city=6
if city=="Acworth": city=7
if city=="Ada": city=8
if city=="Adams": city=9
if city=="Addison": city=10
if city=="Adelanto": city=11
if city=="Adelphi": city=12
if city=="Adirondack": city=13
if city=="Adrian": city=14
if city=="Agoura Hills": city=15
if city=="Aiea": city=16
if city=="Aiken": city=17
if city=="Aitkin": city=18
if city=="Akron": city=19
if city=="Alabaster": city=20
if city=="Alachua": city=21
if city=="Alameda": city=22
if city=="Alamosa": city=23
if city=="Albany": city=24
if city=="Albert City": city=25
if city=="Albertville": city=26
if city=="Albion": city=27
if city=="Albuquerque": city=28
if city=="Alcalde": city=29
if city=="Aleutians West": city=30
if city=="Alexandria": city=31
if city=="Alexandria Bay": city=32
if city=="Alfred": city=33
if city=="Alhambra": city=34
if city=="Aliso Viejo": city=35
if city=="Allen": city=36
if city=="Allentown": city=37
if city=="Alpharetta": city=38
if city=="Alstead": city=39
if city=="Altamonte Springs": city=40
if city=="Altoona": city=41
if city=="Alturas": city=42
if city=="Alum Rock": city=43
if city=="Amarillo": city=44
if city=="Ambler": city=45
if city=="American Canyon": city=46
if city=="American Fork": city=47
if city=="Amery": city=48
if city=="Ames": city=49
if city=="Amesbury": city=50
if city=="Amherst": city=51
if city=="Amite City": city=52
if city=="Amity": city=53
if city=="Anacortes": city=54
if city=="Anaheim": city=55
if city=="Anahola": city=56
if city=="Anchorage": city=57
if city=="Andalusia": city=58
if city=="Anderson": city=59
if city=="Andover": city=60
if city=="Angola": city=61
if city=="Angwin": city=62
if city=="Ann Arbor": city=63
if city=="Annandale": city=64
if city=="Annandale On Hudson": city=65
if city=="Annapolis": city=66
if city=="Anniston": city=67
if city=="Anoka": city=68
if city=="Ansonia": city=69
if city=="Antioch": city=70
if city=="Antrim": city=71
if city=="Apache Junction": city=72
if city=="Apalachicola": city=73
if city=="Apex": city=74
if city=="Apopka": city=75
if city=="Apple Valley": city=76
if city=="Appleton": city=77
if city=="Aptos": city=78
if city=="Aquinnah": city=79
if city=="Ararat": city=80
if city=="Arcadia": city=81
if city=="Arcata": city=82
if city=="Arcola": city=83
if city=="Ardmore": city=84
if city=="Arizona City": city=85
if city=="Arkadelphia": city=86
if city=="Arlington": city=87
if city=="Arlington Heights": city=88
if city=="Arrington": city=89
if city=="Artesia": city=90
if city=="Arvada": city=91
if city=="Asbury Park": city=92
if city=="Ashburn": city=93
if city=="Asheboro": city=94
if city=="Asheville": city=95
if city=="Ashfield": city=96
if city=="Ashland": city=97
if city=="Ashtabula": city=98
if city=="Aspen": city=99
if city=="Astoria": city=100
if city=="Atascadero": city=101
if city=="Athens": city=102
if city=="Athens Clarke County": city=103
if city=="Atlanta": city=104
if city=="Atlanta Decatur": city=105
if city=="Atlantic Beach": city=106
if city=="Atlantic City": city=107
if city=="Attica": city=108
if city=="Auburn": city=109
if city=="Auburn Hills": city=110
if city=="Augusta": city=111
if city=="Aurora": city=112
if city=="Austin": city=113
if city=="Avalon": city=114
if city=="Avenel": city=115
if city=="Averill Park": city=116
if city=="Avery": city=117
if city=="Avon": city=118
if city=="Avondale Estates": city=119
if city=="Ayden": city=120
if city=="Aztec": city=121
if city=="Azusa": city=122
if city=="Babylon": city=123
if city=="Back Swamp": city=124
if city=="Bailey Island": city=125
if city=="Bainbridge": city=126
if city=="Bainbridge Island": city=127
if city=="Baker": city=128
if city=="Bakersfield": city=129
if city=="Baldwinsville": city=130
if city=="Ballston Spa": city=131
if city=="Bally": city=132
if city=="Baltimore": city=133
if city=="Bandera": city=134
if city=="Bandon": city=135
if city=="Bangor": city=136
if city=="Banks": city=137
if city=="Banner Elk": city=138
if city=="Bar Harbor": city=139
if city=="Baraboo": city=140
if city=="Barboursville": city=141
if city=="Barnard": city=142
if city=="Barnegat": city=143
if city=="Barnstable": city=144
if city=="Barnstable Town": city=145
if city=="Barre": city=146
if city=="Barrington": city=147
if city=="Barrow": city=148
if city=="Barrytown": city=149
if city=="Barstow": city=150
if city=="Bartlesville": city=151
if city=="Barton": city=152
if city=="Barwick": city=153
if city=="Batavia": city=154
if city=="Batesville": city=155
if city=="Bath": city=156
if city=="Baton Rouge": city=157
if city=="Battle Creek": city=158
if city=="Battle Mountain": city=159
if city=="Battlement Mesa": city=160
if city=="Baudette": city=161
if city=="Baxter": city=162
if city=="Bay City": city=163
if city=="Bay Minette": city=164
if city=="Bay Shore": city=165
if city=="Bay St. Louis": city=166
if city=="Bayard": city=167
if city=="Bayfield": city=168
if city=="Bayonne": city=169
if city=="Bayport": city=170
if city=="Beach Haven West": city=171
if city=="Beacon": city=172
if city=="Beaufort": city=173
if city=="Beaumont": city=174
if city=="Beaver": city=175
if city=="Beaver Dam": city=176
if city=="Beaver Falls": city=177
if city=="Beaverdam": city=178
if city=="Beaverton": city=179
if city=="Becket": city=180
if city=="Beckville": city=181
if city=="Bedford": city=182
if city=="Bedford   Stuyvesant": city=183
if city=="Bel Air": city=184
if city=="Belchertown": city=185
if city=="Belfast": city=186
if city=="Belgrade": city=187
if city=="Bell Buckle": city=188
if city=="Bellaire": city=189
if city=="Belle Plaine": city=190
if city=="Bellefontaine": city=191
if city=="Belleville": city=192
if city=="Bellevue": city=193
if city=="Bellingham": city=194
if city=="Bellmore": city=195
if city=="Bellows Falls": city=196
if city=="Bellville": city=197
if city=="Belmar": city=198
if city=="Belmont": city=199
if city=="Beloit": city=200
if city=="Belton": city=201
if city=="Beluga": city=202
if city=="Belvidere": city=203
if city=="Bemidji": city=204
if city=="Bend": city=205
if city=="Benicia": city=206
if city=="Bennington": city=207
if city=="Bensalem": city=208
if city=="Benson": city=209
if city=="Benton": city=210
if city=="Benton Harbor": city=211
if city=="Bentonville": city=212
if city=="Berea": city=213
if city=="Beresford": city=214
if city=="Bergenfield": city=215
if city=="Berkeley": city=216
if city=="Berlin": city=217
if city=="Berryville": city=218
if city=="Berthoud": city=219
if city=="Berwyn": city=220
if city=="Bethalto": city=221
if city=="Bethany Beach": city=222
if city=="Bethel Heights": city=223
if city=="Bethel Springs": city=224
if city=="Bethesda": city=225
if city=="Bethlehem": city=226
if city=="Bethpage": city=227
if city=="Bettendorf": city=228
if city=="Beverly": city=229
if city=="Beverly Hills": city=230
if city=="Biddeford": city=231
if city=="Big Bear": city=232
if city=="Big Bear Lake": city=233
if city=="Big Lake": city=234
if city=="Big Pine": city=235
if city=="Big Rapids": city=236
if city=="Big Sandy": city=237
if city=="Big Stone Gap": city=238
if city=="Big Sur": city=239
if city=="Big Timber": city=240
if city=="Billerica": city=241
if city=="Billings": city=242
if city=="Biloxi": city=243
if city=="Binghamton": city=244
if city=="Birch Bay": city=245
if city=="Birmingham": city=246
if city=="Bisbee": city=247
if city=="Bishop": city=248
if city=="Bismarck": city=249
if city=="Black Mountain": city=250
if city=="Blackfoot": city=251
if city=="Blacksburg": city=252
if city=="Bladensburg": city=253
if city=="Blaine": city=254
if city=="Blairsville": city=255
if city=="Blanco": city=256
if city=="Blanding": city=257
if city=="Bloomfield": city=258
if city=="Bloomfield Hills": city=259
if city=="Blooming Grove": city=260
if city=="Bloomington": city=261
if city=="Bloomsburg": city=262
if city=="Blue Hill": city=263
if city=="Blue Lake": city=264
if city=="Blue Ridge": city=265
if city=="Blue Springs": city=266
if city=="Bluff City": city=267
if city=="Bluffton": city=268
if city=="Boalsburg": city=269
if city=="Boca Raton": city=270
if city=="Bodega": city=271
if city=="Boerne": city=272
if city=="Bogalusa": city=273
if city=="Bogota": city=274
if city=="Bohemia": city=275
if city=="Boiling Springs": city=276
if city=="Boise": city=277
if city=="Bolinas": city=278
if city=="Bolingbrook": city=279
if city=="Bonita Springs": city=280
if city=="Bonney Lake": city=281
if city=="Boone": city=282
if city=="Booneville": city=283
if city=="Boonton": city=284
if city=="Boonville": city=285
if city=="Boothbay": city=286
if city=="Boothbay Harbor": city=287
if city=="Bordentown": city=288
if city=="Bossier City": city=289
if city=="Boston": city=290
if city=="Bothell": city=291
if city=="Boulder": city=292
if city=="Boulder City": city=293
if city=="Bountiful": city=294
if city=="Bourne": city=295
if city=="Bowie": city=296
if city=="Bowling Green": city=297
if city=="Boyds": city=298
if city=="Boyes Hot Springs": city=299
if city=="Boyne City": city=300
if city=="Boynton Beach": city=301
if city=="Bozeman": city=302
if city=="Braddock": city=303
if city=="Bradenton": city=304
if city=="Bradford": city=305
if city=="Brainerd": city=306
if city=="Braintree": city=307
if city=="Branchburg": city=308
if city=="Brandenburg": city=309
if city=="Brandon": city=310
if city=="Branford": city=311
if city=="Branson": city=312
if city=="Brattleboro": city=313
if city=="Brawley": city=314
if city=="Brea": city=315
if city=="Breckenridge": city=316
if city=="Bremerton": city=317
if city=="Brentwood": city=318
if city=="Brevard": city=319
if city=="Brewster": city=320
if city=="Brick": city=321
if city=="Brick Township": city=322
if city=="Bridgehampton": city=323
if city=="Bridgeport": city=324
if city=="Bridgewater": city=325
if city=="Bridgewater Township": city=326
if city=="Bridgton": city=327
if city=="Brigham City": city=328
if city=="Brighton": city=329
if city=="Bristol": city=330
if city=="Bristol Bay": city=331
if city=="Bristow": city=332
if city=="Britton": city=333
if city=="Brockton": city=334
if city=="Brodhead": city=335
if city=="Broken Arrow": city=336
if city=="Bronx": city=337
if city=="Bronxville": city=338
if city=="Brookfield": city=339
if city=="Brookings": city=340
if city=="Brookline": city=341
if city=="Brooklyn": city=342
if city=="Brookville": city=343
if city=="Broomfield": city=344
if city=="Brown Deer": city=345
if city=="Brownfield": city=346
if city=="Browning": city=347
if city=="Brownsville": city=348
if city=="Bruneau": city=349
if city=="Bruning": city=350
if city=="Brunswick": city=351
if city=="Bryan": city=352
if city=="Bryant": city=353
if city=="Bryn Mawr": city=354
if city=="Bryson City": city=355
if city=="Buchanan": city=356
if city=="Buckeye": city=357
if city=="Buckfield": city=358
if city=="Buckhannon": city=359
if city=="Buckhead": city=360
if city=="Buckingham": city=361
if city=="Buckley": city=362
if city=="Bucksport": city=363
if city=="Buda": city=364
if city=="Buena Vista": city=365
if city=="Buffalo": city=366
if city=="Buffalo Grove": city=367
if city=="Buford": city=368
if city=="Buies Creek": city=369
if city=="Bullhead": city=370
if city=="Buna": city=371
if city=="Buras": city=372
if city=="Burbank": city=373
if city=="Burien": city=374
if city=="Burleson": city=375
if city=="Burley": city=376
if city=="Burlingame": city=377
if city=="Burlington": city=378
if city=="Burnsville": city=379
if city=="Burtonsville": city=380
if city=="Bushnell": city=381
if city=="Bushwick": city=382
if city=="Butler": city=383
if city=="Butler Township": city=384
if city=="Butte": city=385
if city=="Buzzards Bay": city=386
if city=="Byram": city=387
if city=="Byron": city=388
if city=="Byron Center": city=389
if city=="Cadillac": city=390
if city=="Cadiz": city=391
if city=="Calabasas": city=392
if city=="Calais": city=393
if city=="Caldwell": city=394
if city=="California": city=395
if city=="California City": city=396
if city=="Calumet": city=397
if city=="Camano Island": city=398
if city=="Camarillo": city=399
if city=="Camas": city=400
if city=="Cambridge": city=401
if city=="Camden": city=402
if city=="Cameron": city=403
if city=="Cameron Park": city=404
if city=="Camp Hill": city=405
if city=="Campbell": city=406
if city=="Campo": city=407
if city=="Campton": city=408
if city=="Canaan": city=409
if city=="Canada": city=410
if city=="Canal Fulton": city=411
if city=="Canal Winchester": city=412
if city=="Canandaigua": city=413
if city=="Canby": city=414
if city=="Candor": city=415
if city=="Canoga Park": city=416
if city=="Canton": city=417
if city=="Canyon": city=418
if city=="Canyon Country": city=419
if city=="Canyon Lake": city=420
if city=="Cape Canaveral": city=421
if city=="Cape Coral": city=422
if city=="Cape Girardeau": city=423
if city=="Cape May": city=424
if city=="Capistrano Beach": city=425
if city=="Captain Cook": city=426
if city=="Carbondale": city=427
if city=="Cardington": city=428
if city=="Caribou": city=429
if city=="Carleton": city=430
if city=="Carlisle": city=431
if city=="Carlsbad": city=432
if city=="Carlton": city=433
if city=="Carmel": city=434
if city=="Carmel Valley": city=435
if city=="Carmichael": city=436
if city=="Carmichaels": city=437
if city=="Carrboro": city=438
if city=="Carrollton": city=439
if city=="Carson": city=440
if city=="Carson City": city=441
if city=="Carteret": city=442
if city=="Cary": city=443
if city=="Caseville": city=444
if city=="Casper": city=445
if city=="Cass": city=446
if city=="Cass Lake": city=447
if city=="Castaic": city=448
if city=="Castle Rock": city=449
if city=="Castleton": city=450
if city=="Castro Valley": city=451
if city=="Catonsville": city=452
if city=="Catskill": city=453
if city=="Cave Creek": city=454
if city=="Cazenovia": city=455
if city=="Cedar City": city=456
if city=="Cedar Falls": city=457
if city=="Cedar Hills": city=458
if city=="Cedar Park": city=459
if city=="Cedar Rapids": city=460
if city=="Cedar Springs": city=461
if city=="Cedarville": city=462
if city=="Centennial": city=463
if city=="Centerport": city=464
if city=="Centerville": city=465
if city=="Central": city=466
if city=="Central Coast": city=467
if city=="Central Manchester": city=468
if city=="Central Point": city=469
if city=="Centralia": city=470
if city=="Ceres": city=471
if city=="Cerrillos": city=472
if city=="Cerritos": city=473
if city=="Chadds Ford": city=474
if city=="Chagrin Falls": city=475
if city=="Chalfont": city=476
if city=="Chalmette": city=477
if city=="Chambersburg": city=478
if city=="Champaign": city=479
if city=="Chandler": city=480
if city=="Channing": city=481
if city=="Chapel Hill": city=482
if city=="Chappaqua": city=483
if city=="Charleston": city=484
if city=="Charlevoix": city=485
if city=="Charlotte": city=486
if city=="Charlottesville": city=487
if city=="Chaska": city=488
if city=="Chatham": city=489
if city=="Chatsworth": city=490
if city=="Chattanooga": city=491
if city=="Chehalis": city=492
if city=="Chelmsford": city=493
if city=="Chelsea": city=494
if city=="Cheltenham": city=495
if city=="Cheney": city=496
if city=="Cheraw": city=497
if city=="Cherry Hill": city=498
if city=="Cherry Valley": city=499
if city=="Chesapeake": city=500
if city=="Chester": city=501
if city=="Chester Springs": city=502
if city=="Chesterfield": city=503
if city=="Chesterhill": city=504
if city=="Chesterton": city=505
if city=="Cheswick": city=506
if city=="Cheyenne": city=507
if city=="Chicago": city=508
if city=="Chicago Heights": city=509
if city=="Chicago Metropolitan Area": city=510
if city=="Chickamauga": city=511
if city=="Chico": city=512
if city=="Childress": city=513
if city=="China Grove": city=514
if city=="Chino": city=515
if city=="Chino Hills": city=516
if city=="Chino Valley": city=517
if city=="Chipley": city=518
if city=="Chippewa Falls": city=519
if city=="Chittenango": city=520
if city=="Chittenden": city=521
if city=="Christoval": city=522
if city=="Chula Vista": city=523
if city=="Cincinnati": city=524
if city=="Claremont": city=525
if city=="Clarendon": city=526
if city=="Clarendon Hills": city=527
if city=="Clarion": city=528
if city=="Clarkesville": city=529
if city=="Clarksboro": city=530
if city=="Clarksburg": city=531
if city=="Clarksdale": city=532
if city=="Clarkson": city=533
if city=="Clarkston": city=534
if city=="Clarksville": city=535
if city=="Clayton": city=536
if city=="Clearlake": city=537
if city=="Clearwater": city=538
if city=="Cleland Crossroads": city=539
if city=="Clemson": city=540
if city=="Clermont": city=541
if city=="Cleveland": city=542
if city=="Cleveland Heights": city=543
if city=="Clifton": city=544
if city=="Climax": city=545
if city=="Clinton": city=546
if city=="Clinton Corners": city=547
if city=="Clive": city=548
if city=="Clovis": city=549
if city=="Clyde Park": city=550
if city=="Coal City": city=551
if city=="Coatesville": city=552
if city=="Cochiti Lake": city=553
if city=="Cocoa": city=554
if city=="Cocoa Beach": city=555
if city=="Coconino": city=556
if city=="Coconut Creek": city=557
if city=="Cody": city=558
if city=="Coffeyville": city=559
if city=="Cold Brook": city=560
if city=="Cold Spring": city=561
if city=="Coldspring": city=562
if city=="Colfax": city=563
if city=="College Park": city=564
if city=="College Station": city=565
if city=="Collegedale": city=566
if city=="Collegeville": city=567
if city=="Collingswood": city=568
if city=="Colonia": city=569
if city=="Colonial Beach": city=570
if city=="Colonie": city=571
if city=="Colora": city=572
if city=="Colorado Springs": city=573
if city=="Columbia": city=574
if city=="Columbia Falls": city=575
if city=="Columbus": city=576
if city=="Comfort": city=577
if city=="Commerce": city=578
if city=="Commerce City": city=579
if city=="Como": city=580
if city=="Compton": city=581
if city=="Concord": city=582
if city=="Coney Island": city=583
if city=="Conneaut": city=584
if city=="Conover": city=585
if city=="Continental": city=586
if city=="Conway": city=587
if city=="Conyers": city=588
if city=="Cookeville": city=589
if city=="Cooper City": city=590
if city=="Coos Bay": city=591
if city=="Coral Gables": city=592
if city=="Coral Springs": city=593
if city=="Corbin": city=594
if city=="Cordele": city=595
if city=="Corinth": city=596
if city=="Corning": city=597
if city=="Cornville": city=598
if city=="Cornwall": city=599
if city=="Corona": city=600
if city=="Coronado": city=601
if city=="Corpus Christi": city=602
if city=="Corsicana": city=603
if city=="Corte Madera": city=604
if city=="Cortez": city=605
if city=="Cortlandt Manor": city=606
if city=="Corvallis": city=607
if city=="Cos Cob": city=608
if city=="Costa Mesa": city=609
if city=="Cottage Grove": city=610
if city=="Cottonwood": city=611
if city=="Cotuit": city=612
if city=="Coudersport": city=613
if city=="Coulterville": city=614
if city=="Council": city=615
if city=="Council Bluffs": city=616
if city=="Coupeville": city=617
if city=="Coventry": city=618
if city=="Covina": city=619
if city=="Covington": city=620
if city=="Cozad": city=621
if city=="Cragsmoor": city=622
if city=="Craig": city=623
if city=="Cranbury": city=624
if city=="Cranford": city=625
if city=="Cranston": city=626
if city=="Crescent Lake": city=627
if city=="Cresskill": city=628
if city=="Crested Butte": city=629
if city=="Crestline": city=630
if city=="Crestone": city=631
if city=="Crestview": city=632
if city=="Crestwood": city=633
if city=="Cripple Creek": city=634
if city=="Cromwell": city=635
if city=="Cross Plains": city=636
if city=="Crosslake": city=637
if city=="Croton On Hudson": city=638
if city=="Crow Agency": city=639
if city=="Crown Heights": city=640
if city=="Crown Point": city=641
if city=="Crystal City": city=642
if city=="Crystal Falls": city=643
if city=="Crystal Lake": city=644
if city=="Cullowhee": city=645
if city=="Culpeper": city=646
if city=="Culver City": city=647
if city=="Cumberland": city=648
if city=="Cumming": city=649
if city=="Cupertino": city=650
if city=="Custer": city=651
if city=="Cut Off": city=652
if city=="Cutchogue": city=653
if city=="Cuyahoga Falls": city=654
if city=="Cypress": city=655
if city=="Dade City": city=656
if city=="Dagsboro": city=657
if city=="Dahlgren": city=658
if city=="Dahlonega": city=659
if city=="Dallas": city=660
if city=="Dalton": city=661
if city=="Daly City": city=662
if city=="Dalzell": city=663
if city=="Damascus": city=664
if city=="Dana Point": city=665
if city=="Danbury": city=666
if city=="Danvers": city=667
if city=="Danville": city=668
if city=="Daphne": city=669
if city=="Dartmouth": city=670
if city=="Davenport": city=671
if city=="Davie": city=672
if city=="Davis": city=673
if city=="Davison": city=674
if city=="Dawson Springs": city=675
if city=="Dawsonville": city=676
if city=="Dayton": city=677
if city=="Daytona Beach": city=678
if city=="De Bary": city=679
if city=="De Forest": city=680
if city=="De Funiak Springs": city=681
if city=="De Kalb": city=682
if city=="De Land": city=683
if city=="De Mossville": city=684
if city=="De Motte": city=685
if city=="De Pere": city=686
if city=="De Ridder": city=687
if city=="Deadhorse": city=688
if city=="Dearborn": city=689
if city=="Dearborn Heights": city=690
if city=="Death Valley": city=691
if city=="Decatur": city=692
if city=="Decorah": city=693
if city=="Deep River": city=694
if city=="Deerfield": city=695
if city=="Deerfield Beach": city=696
if city=="Defiance": city=697
if city=="Del Mar": city=698
if city=="Del Rio": city=699
if city=="Delancey": city=700
if city=="Delano": city=701
if city=="Delavan": city=702
if city=="Delaware": city=703
if city=="Delaware Water Gap": city=704
if city=="Delhi": city=705
if city=="Dell City": city=706
if city=="Delran": city=707
if city=="Delray Beach": city=708
if city=="Delta": city=709
if city=="Delta Junction": city=710
if city=="Deltona": city=711
if city=="Denali": city=712
if city=="Denison": city=713
if city=="Denmark": city=714
if city=="Denton": city=715
if city=="Denver": city=716
if city=="Denville": city=717
if city=="Derry": city=718
if city=="Des Moines": city=719
if city=="Des Plaines": city=720
if city=="Desert": city=721
if city=="Desert Aire": city=722
if city=="Desert Hot Springs": city=723
if city=="Desloge": city=724
if city=="Destin": city=725
if city=="Detroit": city=726
if city=="Diamond Bar": city=727
if city=="Dickinson": city=728
if city=="Dillon": city=729
if city=="Dillsburg": city=730
if city=="Dinuba": city=731
if city=="Dix Hills": city=732
if city=="Dixon": city=733
if city=="Dodgeville": city=734
if city=="Dorchester": city=735
if city=="Dormont": city=736
if city=="Dorr": city=737
if city=="Dothan": city=738
if city=="Douglasville": city=739
if city=="Dover": city=740
if city=="Downers Grove": city=741
if city=="Downey": city=742
if city=="Downingtown": city=743
if city=="Doylestown": city=744
if city=="Draper": city=745
if city=="Drummond": city=746
if city=="Dublin": city=747
if city=="Dubois": city=748
if city=="Dubuque": city=749
if city=="Duck Key": city=750
if city=="Dudley": city=751
if city=="Dulac": city=752
if city=="Duluth": city=753
if city=="Dumont": city=754
if city=="Dunedin": city=755
if city=="Dunmore": city=756
if city=="Durango": city=757
if city=="Durant": city=758
if city=="Durham": city=759
if city=="Duvall": city=760
if city=="Dyer": city=761
if city=="Eagan": city=762
if city=="Eagle": city=763
if city=="Eagle Butte": city=764
if city=="Eagle Mountain": city=765
if city=="Eagleville": city=766
if city=="Earth": city=767
if city=="Easley": city=768
if city=="East": city=769
if city=="East Aurora": city=770
if city=="East Brunswick": city=771
if city=="East Greenbush": city=772
if city=="East Greenwich": city=773
if city=="East Hampton": city=774
if city=="East Hanover": city=775
if city=="East Harlem": city=776
if city=="East Jordan": city=777
if city=="East Lansing": city=778
if city=="East Los Angeles": city=779
if city=="East Meadow": city=780
if city=="East Nashville": city=781
if city=="East Northport": city=782
if city=="East Orange": city=783
if city=="East Palo Alto": city=784
if city=="East Peoria": city=785
if city=="East Point": city=786
if city=="East Providence": city=787
if city=="East St Louis": city=788
if city=="East Stroudsburg": city=789
if city=="East Village": city=790
if city=="East Wakefield": city=791
if city=="Eastampton": city=792
if city=="Eastford": city=793
if city=="Easthampton": city=794
if city=="Eastlake": city=795
if city=="Easton": city=796
if city=="Eastpoint": city=797
if city=="Eau Claire": city=798
if city=="Eden": city=799
if city=="Eden Prairie": city=800
if city=="Edgefield": city=801
if city=="Edgerton": city=802
if city=="Edgewater": city=803
if city=="Edinboro": city=804
if city=="Edinburg": city=805
if city=="Edison": city=806
if city=="Edmond": city=807
if city=="Edmonds": city=808
if city=="Edon": city=809
if city=="Edwards": city=810
if city=="Effingham": city=811
if city=="Egg Harbor Township": city=812
if city=="Eglin Afb": city=813
if city=="Egremont": city=814
if city=="El Cajon": city=815
if city=="El Centro": city=816
if city=="El Cerrito": city=817
if city=="El Dorado": city=818
if city=="El Monte": city=819
if city=="El Morro": city=820
if city=="El Paso": city=821
if city=="El Portal": city=822
if city=="El Reno": city=823
if city=="Elberta": city=824
if city=="Elgin": city=825
if city=="Eliot": city=826
if city=="Elizabeth": city=827
if city=="Elizabethton": city=828
if city=="Elizabethtown": city=829
if city=="Elk": city=830
if city=="Elk Grove": city=831
if city=="Elk Grove Village": city=832
if city=="Elkhart": city=833
if city=="Elkhorn": city=834
if city=="Elkin": city=835
if city=="Elkins": city=836
if city=="Elkmont": city=837
if city=="Elkridge": city=838
if city=="Elkton": city=839
if city=="Ellensburg": city=840
if city=="Ellenville": city=841
if city=="Ellettsville": city=842
if city=="Ellicott City": city=843
if city=="Ellijay": city=844
if city=="Ellsworth": city=845
if city=="Elm Grove": city=846
if city=="Elmhurst": city=847
if city=="Elmore": city=848
if city=="Elon": city=849
if city=="Eloy": city=850
if city=="Elroy": city=851
if city=="Elverson": city=852
if city=="Ely": city=853
if city=="Elyria": city=854
if city=="Emerson": city=855
if city=="Emeryville": city=856
if city=="Emmett": city=857
if city=="Emmitsburg": city=858
if city=="Emporia": city=859
if city=="Encinitas": city=860
if city=="Endicott": city=861
if city=="Enfield": city=862
if city=="Englewood": city=863
if city=="Englewood Cliffs": city=864
if city=="Enosburg Falls": city=865
if city=="Enterprise": city=866
if city=="Enumclaw": city=867
if city=="Ephraim": city=868
if city=="Erath": city=869
if city=="Erie": city=870
if city=="Erwin": city=871
if city=="Escanaba": city=872
if city=="Escondido": city=873
if city=="Esopus": city=874
if city=="Espanola": city=875
if city=="Essex": city=876
if city=="Essex Junction": city=877
if city=="Estero": city=878
if city=="Estes Park": city=879
if city=="Etters": city=880
if city=="Euclid": city=881
if city=="Eugene": city=882
if city=="Euless": city=883
if city=="Eureka": city=884
if city=="Eureka Springs": city=885
if city=="Eustis": city=886
if city=="Evanston": city=887
if city=="Evansville": city=888
if city=="Everett": city=889
if city=="Everglades": city=890
if city=="Evergreen": city=891
if city=="Ewa Beach": city=892
if city=="Ewing": city=893
if city=="Exeter": city=894
if city=="Exton": city=895
if city=="Factoryville": city=896
if city=="Fair Lawn": city=897
if city=="Fair Oaks": city=898
if city=="Fairbanks": city=899
if city=="Fairborn": city=900
if city=="Fairburn": city=901
if city=="Fairfax": city=902
if city=="Fairfield": city=903
if city=="Fairhope": city=904
if city=="Fairlee": city=905
if city=="Fairmont": city=906
if city=="Fairview": city=907
if city=="Fall River": city=908
if city=="Fallbrook": city=909
if city=="Falling Waters": city=910
if city=="Fallon": city=911
if city=="Falls Church": city=912
if city=="Falmouth": city=913
if city=="Fanwood": city=914
if city=="Far Rockaway": city=915
if city=="Fargo": city=916
if city=="Faribault": city=917
if city=="Farmingdale": city=918
if city=="Farmington": city=919
if city=="Farmville": city=920
if city=="Farwell": city=921
if city=="Faulkton": city=922
if city=="Fayetteville": city=923
if city=="Federal Heights": city=924
if city=="Feeding Hills": city=925
if city=="Fernandina Beach": city=926
if city=="Ferndale": city=927
if city=="Ferriday": city=928
if city=="Ferris": city=929
if city=="Fillmore": city=930
if city=="Findlay": city=931
if city=="Fish Creek": city=932
if city=="Fishers": city=933
if city=="Fishkill": city=934
if city=="Fitchburg": city=935
if city=="Fitzwilliam": city=936
if city=="Flagler Beach": city=937
if city=="Flagstaff": city=938
if city=="Flanders": city=939
if city=="Flatwoods": city=940
if city=="Fleetwood": city=941
if city=="Flemington": city=942
if city=="Flint": city=943
if city=="Flintstone": city=944
if city=="Florence": city=945
if city=="Floresville": city=946
if city=="Florham Park": city=947
if city=="Florida": city=948
if city=="Florissant": city=949
if city=="Flovilla": city=950
if city=="Flower Mound": city=951
if city=="Flowery Branch": city=952
if city=="Floyd": city=953
if city=="Flushing": city=954
if city=="Folly Beach": city=955
if city=="Folsom": city=956
if city=="Fontana": city=957
if city=="Forest": city=958
if city=="Forest Grove": city=959
if city=="Forest Hill": city=960
if city=="Forest Hills": city=961
if city=="Forest Lake": city=962
if city=="Forest Park": city=963
if city=="Fork Union": city=964
if city=="Forks": city=965
if city=="Forney": city=966
if city=="Forrest City": city=967
if city=="Fort Bliss": city=968
if city=="Fort Bragg": city=969
if city=="Fort Collins": city=970
if city=="Fort Dix": city=971
if city=="Fort Fairfield": city=972
if city=="Fort Lauderdale": city=973
if city=="Fort Lee": city=974
if city=="Fort Lewis": city=975
if city=="Fort Mill": city=976
if city=="Fort Myers": city=977
if city=="Fort Payne": city=978
if city=="Fort Pierce": city=979
if city=="Fort Polk": city=980
if city=="Fort Sill": city=981
if city=="Fort Smith": city=982
if city=="Fort Walton Beach": city=983
if city=="Fort Wayne": city=984
if city=="Fort White": city=985
if city=="Fort Worth": city=986
if city=="Fortuna": city=987
if city=="Foster": city=988
if city=="Fountain Hills": city=989
if city=="Fountain Valley": city=990
if city=="Fowler": city=991
if city=="Fox Lake": city=992
if city=="Framingham": city=993
if city=="Frankfort": city=994
if city=="Franklin": city=995
if city=="Franklin Lakes": city=996
if city=="Franklin Park": city=997
if city=="Franklin Square": city=998
if city=="Frederick": city=999
if city=="Fredericksburg": city=1000
if city=="Frederickson": city=1001
if city=="Fredonia": city=1002
if city=="Freehold": city=1003
if city=="Freeland": city=1004
if city=="Freeport": city=1005
if city=="Fremont": city=1006
if city=="French Camp": city=1007
if city=="Frenchtown": city=1008
if city=="Fresno": city=1009
if city=="Friday Harbor": city=1010
if city=="Friona": city=1011
if city=="Frisco": city=1012
if city=="Front Royal": city=1013
if city=="Frostburg": city=1014
if city=="Frostproof": city=1015
if city=="Fullerton": city=1016
if city=="Fulshear": city=1017
if city=="Fulton": city=1018
if city=="Fuquay Varina": city=1019
if city=="Gainesville": city=1020
if city=="Gaithersburg": city=1021
if city=="Galisteo": city=1022
if city=="Gallatin Gateway": city=1023
if city=="Gallipolis": city=1024
if city=="Gallup": city=1025
if city=="Galveston": city=1026
if city=="Garden City": city=1027
if city=="Garden Grove": city=1028
if city=="Gardena": city=1029
if city=="Gardiner": city=1030
if city=="Gardner": city=1031
if city=="Gardnerville": city=1032
if city=="Garland": city=1033
if city=="Gary": city=1034
if city=="Gas City": city=1035
if city=="Gaston": city=1036
if city=="Gastonia": city=1037
if city=="Gatlinburg": city=1038
if city=="Gayville": city=1039
if city=="Geff": city=1040
if city=="Geneseo": city=1041
if city=="Geneva": city=1042
if city=="George": city=1043
if city=="Georgetown": city=1044
if city=="Gering": city=1045
if city=="Gerlach Empire": city=1046
if city=="Germantown": city=1047
if city=="Germany": city=1048
if city=="Gettysburg": city=1049
if city=="Ghent": city=1050
if city=="Gig Harbor": city=1051
if city=="Gilbert": city=1052
if city=="Gilgo Oak Beach Captree": city=1053
if city=="Gilkey": city=1054
if city=="Gillette": city=1055
if city=="Gilmanton Iw": city=1056
if city=="Gilroy": city=1057
if city=="Glacier National Park": city=1058
if city=="Glasgow": city=1059
if city=="Glassboro": city=1060
if city=="Glen Allen": city=1061
if city=="Glen Burnie": city=1062
if city=="Glen Cove": city=1063
if city=="Glen Ellyn": city=1064
if city=="Glen Rock": city=1065
if city=="Glendale": city=1066
if city=="Glendora": city=1067
if city=="Glenolden": city=1068
if city=="Glens Falls": city=1069
if city=="Glenside": city=1070
if city=="Glenview": city=1071
if city=="Globe": city=1072
if city=="Gloucester": city=1073
if city=="Gloucester City": city=1074
if city=="Glyndon": city=1075
if city=="Gold Beach": city=1076
if city=="Golden": city=1077
if city=="Goldens Bridge": city=1078
if city=="Goleta": city=1079
if city=="Goodrich": city=1080
if city=="Goshen": city=1081
if city=="Grafton": city=1082
if city=="Graham": city=1083
if city=="Grain Valley": city=1084
if city=="Granada Hills": city=1085
if city=="Granby": city=1086
if city=="Grand Canyon": city=1087
if city=="Grand Forks": city=1088
if city=="Grand Haven": city=1089
if city=="Grand Island": city=1090
if city=="Grand Junction": city=1091
if city=="Grand Lake": city=1092
if city=="Grand Prairie": city=1093
if city=="Grand Rapids": city=1094
if city=="Grand Rapids Charter Township": city=1095
if city=="Grandview": city=1096
if city=="Granger": city=1097
if city=="Grants Pass": city=1098
if city=="Granville": city=1099
if city=="Grapevine": city=1100
if city=="Grass Valley": city=1101
if city=="Great Barrington": city=1102
if city=="Great Bend": city=1103
if city=="Great Falls": city=1104
if city=="Great Neck": city=1105
if city=="Greeley": city=1106
if city=="Green": city=1107
if city=="Green Bay": city=1108
if city=="Green Brook": city=1109
if city=="Green Lake": city=1110
if city=="Green River": city=1111
if city=="Greenacres": city=1112
if city=="Greenbelt": city=1113
if city=="Greenbrier": city=1114
if city=="Greencastle": city=1115
if city=="Greeneville": city=1116
if city=="Greenfield": city=1117
if city=="Greenland": city=1118
if city=="Greenlawn": city=1119
if city=="Greenleaf": city=1120
if city=="Greenpoint": city=1121
if city=="Greenport": city=1122
if city=="Greensboro": city=1123
if city=="Greensburg": city=1124
if city=="Greenville": city=1125
if city=="Greenwich": city=1126
if city=="Greenwood": city=1127
if city=="Greenwood Lake": city=1128
if city=="Gresham": city=1129
if city=="Griffin": city=1130
if city=="Groton": city=1131
if city=="Grove City": city=1132
if city=="Grovetown": city=1133
if city=="Guadalupe": city=1134
if city=="Guilford Center": city=1135
if city=="Gulfport": city=1136
if city=="Gun Barrel City": city=1137
if city=="Guntersville": city=1138
if city=="Guymon": city=1139
if city=="Hacienda Heights": city=1140
if city=="Hackensack": city=1141
if city=="Hackettstown": city=1142
if city=="Haddon Heights": city=1143
if city=="Haddonfield": city=1144
if city=="Hadley": city=1145
if city=="Hagerstown": city=1146
if city=="Haiku": city=1147
if city=="Haines City": city=1148
if city=="Haledon": city=1149
if city=="Haleiwa": city=1150
if city=="Half Moon Bay": city=1151
if city=="Halifax": city=1152
if city=="Hallandale": city=1153
if city=="Hallettsville": city=1154
if city=="Hallowell": city=1155
if city=="Hamburg": city=1156
if city=="Hamden": city=1157
if city=="Hamilton": city=1158
if city=="Hamilton Township": city=1159
if city=="Hammond": city=1160
if city=="Hammondsport": city=1161
if city=="Hammonton": city=1162
if city=="Hampstead": city=1163
if city=="Hampton": city=1164
if city=="Hamtramck": city=1165
if city=="Hancock": city=1166
if city=="Hannibal": city=1167
if city=="Hanover": city=1168
if city=="Hanover Park": city=1169
if city=="Harbor Springs": city=1170
if city=="Hardwick": city=1171
if city=="Hardyston": city=1172
if city=="Harlem": city=1173
if city=="Harleysville": city=1174
if city=="Harlingen San Benito": city=1175
if city=="Harmony": city=1176
if city=="Harpers Ferry": city=1177
if city=="Harrisburg": city=1178
if city=="Harrison": city=1179
if city=="Harrisonburg": city=1180
if city=="Harrisville": city=1181
if city=="Hartford": city=1182
if city=="Hartland": city=1183
if city=="Harvey": city=1184
if city=="Harwich Center": city=1185
if city=="Hastings On Hudson": city=1186
if city=="Hatboro": city=1187
if city=="Hatfield": city=1188
if city=="Hatteras": city=1189
if city=="Hattiesburg": city=1190
if city=="Havelock": city=1191
if city=="Haverstraw": city=1192
if city=="Havre De Grace": city=1193
if city=="Hawaiian Beaches": city=1194
if city=="Hawesville": city=1195
if city=="Hawi": city=1196
if city=="Hawley": city=1197
if city=="Hawthorne": city=1198
if city=="Hays": city=1199
if city=="Haysville": city=1200
if city=="Hayward": city=1201
if city=="Hazard": city=1202
if city=="Hazleton": city=1203
if city=="Healdsburg": city=1204
if city=="Heart Butte": city=1205
if city=="Heber": city=1206
if city=="Hebron": city=1207
if city=="Hector": city=1208
if city=="Helen": city=1209
if city=="Helena": city=1210
if city=="Hellam": city=1211
if city=="Hemet": city=1212
if city=="Hempstead": city=1213
if city=="Henderson": city=1214
if city=="Hendersonville": city=1215
if city=="Henniker": city=1216
if city=="Herkimer": city=1217
if city=="Hermiston": city=1218
if city=="Hermitage": city=1219
if city=="Hermosa Beach": city=1220
if city=="Herndon": city=1221
if city=="Hershey": city=1222
if city=="Hertford": city=1223
if city=="Hesperia": city=1224
if city=="Hettinger": city=1225
if city=="Hewitt": city=1226
if city=="Hickory": city=1227
if city=="Hicksville": city=1228
if city=="High Falls": city=1229
if city=="High Island": city=1230
if city=="High Point": city=1231
if city=="High Springs": city=1232
if city=="Highland": city=1233
if city=="Highland Mills": city=1234
if city=="Highland Park": city=1235
if city=="Highlands": city=1236
if city=="Highlands Ranch": city=1237
if city=="Hightstown": city=1238
if city=="Hill City": city=1239
if city=="Hilliard": city=1240
if city=="Hillsboro": city=1241
if city=="Hillsborough": city=1242
if city=="Hillsdale": city=1243
if city=="Hillside": city=1244
if city=="Hilo": city=1245
if city=="Hilton Head Island": city=1246
if city=="Hinesburg": city=1247
if city=="Hingham": city=1248
if city=="Hinsdale": city=1249
if city=="Hobe Sound": city=1250
if city=="Hoboken": city=1251
if city=="Holgate": city=1252
if city=="Holland": city=1253
if city=="Hollis": city=1254
if city=="Hollister": city=1255
if city=="Hollywood": city=1256
if city=="Holmdel Township": city=1257
if city=="Holtsville": city=1258
if city=="Holyoke": city=1259
if city=="Homeland": city=1260
if city=="Homer": city=1261
if city=="Homosassa": city=1262
if city=="Honeoye Falls": city=1263
if city=="Honeyville": city=1264
if city=="Honokaa": city=1265
if city=="Honolulu": city=1266
if city=="Hood River": city=1267
if city=="Hookstown": city=1268
if city=="Hoonah": city=1269
if city=="Hoopa": city=1270
if city=="Hoover": city=1271
if city=="Hopatcong": city=1272
if city=="Hopewell Junction": city=1273
if city=="Hopkins": city=1274
if city=="Hopkinsville": city=1275
if city=="Hoquiam": city=1276
if city=="Horseheads": city=1277
if city=="Horton": city=1278
if city=="Hot Springs": city=1279
if city=="Houghton": city=1280
if city=="Houlton": city=1281
if city=="Houston": city=1282
if city=="Howard": city=1283
if city=="Howell": city=1284
if city=="Hualapai": city=1285
if city=="Huber Heights": city=1286
if city=="Hubertus": city=1287
if city=="Hudson": city=1288
if city=="Hugo": city=1289
if city=="Hull": city=1290
if city=="Hummelstown": city=1291
if city=="Hunter": city=1292
if city=="Huntersville": city=1293
if city=="Huntington": city=1294
if city=="Huntington Beach": city=1295
if city=="Huntington Station": city=1296
if city=="Huntington Woods": city=1297
if city=="Huntingtown": city=1298
if city=="Huntsville": city=1299
if city=="Hurlock": city=1300
if city=="Hurricane": city=1301
if city=="Hurst": city=1302
if city=="Hutchinson": city=1303
if city=="Hutchinson Island South": city=1304
if city=="Hyannis": city=1305
if city=="Hyattsville": city=1306
if city=="Hyde Park": city=1307
if city=="Hyden": city=1308
if city=="Idaho City": city=1309
if city=="Idaho Falls": city=1310
if city=="Idyllwild": city=1311
if city=="Ilion": city=1312
if city=="Imlay": city=1313
if city=="Imlay City": city=1314
if city=="Independence": city=1315
if city=="Indian Harbour Beach": city=1316
if city=="Indian River": city=1317
if city=="Indiana": city=1318
if city=="Indianapolis": city=1319
if city=="Indianola": city=1320
if city=="Indio": city=1321
if city=="Inglewood": city=1322
if city=="Inkster": city=1323
if city=="Inlet": city=1324
if city=="Interior": city=1325
if city=="Interlochen": city=1326
if city=="Inwood": city=1327
if city=="Ionia": city=1328
if city=="Iowa City": city=1329
if city=="Ipswich": city=1330
if city=="Iron Mountain": city=1331
if city=="Iron Range": city=1332
if city=="Iron River": city=1333
if city=="Ironton": city=1334
if city=="Irvine": city=1335
if city=="Irving": city=1336
if city=="Isla Vista": city=1337
if city=="Islip": city=1338
if city=="Issaquah": city=1339
if city=="Italy": city=1340
if city=="Ithaca": city=1341
if city=="Ivanhoe": city=1342
if city=="Ivyland": city=1343
if city=="Jackson": city=1344
if city=="Jacksonport": city=1345
if city=="Jacksonville": city=1346
if city=="Jacksonville Beach": city=1347
if city=="Jamaica Plain": city=1348
if city=="Jamestown": city=1349
if city=="Jane Lew": city=1350
if city=="Jasper": city=1351
if city=="Jay": city=1352
if city=="Jefferson City": city=1353
if city=="Jeffersonville": city=1354
if city=="Jensen Beach": city=1355
if city=="Jerome": city=1356
if city=="Jersey": city=1357
if city=="Jersey City": city=1358
if city=="Jessup": city=1359
if city=="Jewett City": city=1360
if city=="Jim Thorpe": city=1361
if city=="Johnson": city=1362
if city=="Johnson City": city=1363
if city=="Johnston": city=1364
if city=="Johnstown": city=1365
if city=="Joliet": city=1366
if city=="Jolo": city=1367
if city=="Jonesboro": city=1368
if city=="Jonesborough": city=1369
if city=="Joplin": city=1370
if city=="Joshua Tree": city=1371
if city=="Julian": city=1372
if city=="Junction City": city=1373
if city=="Juneau": city=1374
if city=="Jupiter": city=1375
if city=="Kahuku": city=1376
if city=="Kahului": city=1377
if city=="Kailua": city=1378
if city=="Kailua Kona": city=1379
if city=="Kalamazoo": city=1380
if city=="Kalispell": city=1381
if city=="Kamuela": city=1382
if city=="Kanab": city=1383
if city=="Kane": city=1384
if city=="Kankakee": city=1385
if city=="Kannapolis": city=1386
if city=="Kansas City": city=1387
if city=="Kapaa": city=1388
if city=="Kapolei": city=1389
if city=="Katy": city=1390
if city=="Kaukauna": city=1391
if city=="Kawaihae": city=1392
if city=="Kaysville": city=1393
if city=="Keaau": city=1394
if city=="Kearney": city=1395
if city=="Kearny": city=1396
if city=="Keene": city=1397
if city=="Kelso": city=1398
if city=="Kenai": city=1399
if city=="Kenesaw": city=1400
if city=="Kenmore": city=1401
if city=="Kennebunk": city=1402
if city=="Kennebunkport": city=1403
if city=="Kennesaw": city=1404
if city=="Kennewick": city=1405
if city=="Kenosha": city=1406
if city=="Kensal": city=1407
if city=="Kensington": city=1408
if city=="Kent": city=1409
if city=="Kentfield": city=1410
if city=="Kentwood": city=1411
if city=="Keokuk": city=1412
if city=="Kernersville": city=1413
if city=="Kersey": city=1414
if city=="Ketchum": city=1415
if city=="Kettering": city=1416
if city=="Kettle Falls": city=1417
if city=="Key Biscayne": city=1418
if city=="Key Largo": city=1419
if city=="Key West": city=1420
if city=="Keyport": city=1421
if city=="Kihei": city=1422
if city=="Kilauea": city=1423
if city=="Kilgore": city=1424
if city=="Killeen": city=1425
if city=="Kinderhook": city=1426
if city=="King": city=1427
if city=="King City": city=1428
if city=="King Of Prussia": city=1429
if city=="Kingman": city=1430
if city=="Kingsbury": city=1431
if city=="Kingsland": city=1432
if city=="Kingsport": city=1433
if city=="Kingston": city=1434
if city=="Kinnelon": city=1435
if city=="Kinston": city=1436
if city=="Kirkland": city=1437
if city=="Kirkville": city=1438
if city=="Kirkwood": city=1439
if city=="Kissimmee": city=1440
if city=="Kittery": city=1441
if city=="Klamath Falls": city=1442
if city=="Knoxville": city=1443
if city=="Kodiak": city=1444
if city=="Kokomo": city=1445
if city=="Kremmling": city=1446
if city=="Kula": city=1447
if city=="Kutztown": city=1448
if city=="Kwethluk": city=1449
if city=="Kyle": city=1450
if city=="La Crescenta": city=1451
if city=="La Grande": city=1452
if city=="La Grange": city=1453
if city=="La Jolla": city=1454
if city=="La Luz": city=1455
if city=="La Mesa": city=1456
if city=="La Mirada": city=1457
if city=="La Pointe": city=1458
if city=="La Porte": city=1459
if city=="La Puente": city=1460
if city=="La Quinta": city=1461
if city=="Lacey": city=1462
if city=="Ladera Ranch": city=1463
if city=="Lafayette": city=1464
if city=="Lago Vista": city=1465
if city=="Laguna Beach": city=1466
if city=="Laguna Hills": city=1467
if city=="Laguna Niguel": city=1468
if city=="Lahaina": city=1469
if city=="Laie": city=1470
if city=="Lake Arrowhead": city=1471
if city=="Lake Benton": city=1472
if city=="Lake Charles": city=1473
if city=="Lake City": city=1474
if city=="Lake Elsinore": city=1475
if city=="Lake Forest": city=1476
if city=="Lake Geneva": city=1477
if city=="Lake George": city=1478
if city=="Lake Helen": city=1479
if city=="Lake Hopatcong": city=1480
if city=="Lake Jackson": city=1481
if city=="Lake Mary": city=1482
if city=="Lake Orion": city=1483
if city=="Lake Oswego": city=1484
if city=="Lake Ozark": city=1485
if city=="Lake Placid": city=1486
if city=="Lake Worth": city=1487
if city=="Lake Zurich": city=1488
if city=="Lakeland": city=1489
if city=="Lakeside": city=1490
if city=="Lakeville": city=1491
if city=="Lakewood": city=1492
if city=="Lambertville": city=1493
if city=="Lame Deer": city=1494
if city=="Lancaster": city=1495
if city=="Landenberg": city=1496
if city=="Langhorne": city=1497
if city=="Lansdale": city=1498
if city=="Lansing": city=1499
if city=="Lapeer": city=1500
if city=="Laramie": city=1501
if city=="Laredo": city=1502
if city=="Largo": city=1503
if city=="Larkspur": city=1504
if city=="Las Cruces": city=1505
if city=="Las Vegas": city=1506
if city=="Latrobe": city=1507
if city=="Laurel": city=1508
if city=="Laurence Harbor": city=1509
if city=="Lawndale": city=1510
if city=="Lawrence": city=1511
if city=="Lawrenceburg": city=1512
if city=="Lawrenceville": city=1513
if city=="Lawton": city=1514
if city=="Layton": city=1515
if city=="Lead": city=1516
if city=="Leadville": city=1517
if city=="League City": city=1518
if city=="Leander": city=1519
if city=="Leavenworth": city=1520
if city=="Lebanon": city=1521
if city=="Lee": city=1522
if city=="Leesburg": city=1523
if city=="Leesville": city=1524
if city=="Lehi": city=1525
if city=="Lehigh Acres": city=1526
if city=="Leicester": city=1527
if city=="Leitchfield": city=1528
if city=="Lemoore": city=1529
if city=="Lenexa": city=1530
if city=="Lennox": city=1531
if city=="Lenox": city=1532
if city=="Leominster": city=1533
if city=="Leonard": city=1534
if city=="Leonardtown": city=1535
if city=="Leonia": city=1536
if city=="Leucadia": city=1537
if city=="Leverett": city=1538
if city=="Levittown": city=1539
if city=="Lewisburg": city=1540
if city=="Lewiston": city=1541
if city=="Lewistown": city=1542
if city=="Lewisville": city=1543
if city=="Lexington": city=1544
if city=="Leyden": city=1545
if city=="Ligonier": city=1546
if city=="Lilburn": city=1547
if city=="Lincoln": city=1548
if city=="Lincolnville": city=1549
if city=="Linden": city=1550
if city=="Lindenhurst": city=1551
if city=="Lindenwold": city=1552
if city=="Lindsay": city=1553
if city=="Lisbon Falls": city=1554
if city=="Lisle": city=1555
if city=="Litchfield": city=1556
if city=="Litchfield Park": city=1557
if city=="Lithonia": city=1558
if city=="Little Canada": city=1559
if city=="Little Egg Harbor": city=1560
if city=="Little Havana": city=1561
if city=="Little River": city=1562
if city=="Little Rock": city=1563
if city=="Littlefield": city=1564
if city=="Littlerock": city=1565
if city=="Littleton": city=1566
if city=="Livermore": city=1567
if city=="Liverpool": city=1568
if city=="Livingston": city=1569
if city=="Livonia": city=1570
if city=="Llano": city=1571
if city=="Lodi": city=1572
if city=="Logan": city=1573
if city=="Logansport": city=1574
if city=="Loganville": city=1575
if city=="Loma Linda": city=1576
if city=="Lombard": city=1577
if city=="Lompoc": city=1578
if city=="Londonderry": city=1579
if city=="Long Beach": city=1580
if city=="Long Branch": city=1581
if city=="Long Island": city=1582
if city=="Long Island City": city=1583
if city=="Longmont": city=1584
if city=="Longview": city=1585
if city=="Longwood": city=1586
if city=="Loomis": city=1587
if city=="Lopez Island": city=1588
if city=="Lorain": city=1589
if city=="Lorton": city=1590
if city=="Los Alamitos": city=1591
if city=="Los Alamos": city=1592
if city=="Los Altos": city=1593
if city=="Los Angeles": city=1594
if city=="Los Banos": city=1595
if city=="Los Gatos": city=1596
if city=="Louisville": city=1597
if city=="Loveladies": city=1598
if city=="Loveland": city=1599
if city=="Lowell": city=1600
if city=="Lower Brule": city=1601
if city=="Lower East Side": city=1602
if city=="Loxley": city=1603
if city=="Loyalton": city=1604
if city=="Lubbock": city=1605
if city=="Ludington": city=1606
if city=="Ludlow": city=1607
if city=="Lufkin": city=1608
if city=="Lumberton": city=1609
if city=="Lumberville": city=1610
if city=="Luna": city=1611
if city=="Lunenburg": city=1612
if city=="Luray": city=1613
if city=="Luverne": city=1614
if city=="Luzerne": city=1615
if city=="Lyme": city=1616
if city=="Lynbrook": city=1617
if city=="Lynchburg": city=1618
if city=="Lynden": city=1619
if city=="Lynn": city=1620
if city=="Lynn Haven": city=1621
if city=="Lynnwood": city=1622
if city=="Lyons": city=1623
if city=="Lytle Creek": city=1624
if city=="Mabton": city=1625
if city=="Macclenny": city=1626
if city=="Macedon": city=1627
if city=="Machias": city=1628
if city=="Mackinac Island": city=1629
if city=="Macomb": city=1630
if city=="Macon": city=1631
if city=="Macungie": city=1632
if city=="Madeira": city=1633
if city=="Madeira Beach": city=1634
if city=="Madison": city=1635
if city=="Madrid": city=1636
if city=="Mahopac": city=1637
if city=="Mahwah": city=1638
if city=="Maine": city=1639
if city=="Maineville": city=1640
if city=="Makawao": city=1641
if city=="Malibu": city=1642
if city=="Malvern": city=1643
if city=="Mamaroneck": city=1644
if city=="Mammoth Lakes": city=1645
if city=="Manahawkin": city=1646
if city=="Manalapan": city=1647
if city=="Manasquan": city=1648
if city=="Manassas": city=1649
if city=="Mancelona": city=1650
if city=="Manchester": city=1651
if city=="Manchester By The Sea": city=1652
if city=="Mandeville": city=1653
if city=="Manhattan": city=1654
if city=="Manhattan Beach": city=1655
if city=="Manitou Springs": city=1656
if city=="Manitowoc": city=1657
if city=="Mankato": city=1658
if city=="Mannford": city=1659
if city=="Manning": city=1660
if city=="Mansfield": city=1661
if city=="Manteca": city=1662
if city=="Mantua": city=1663
if city=="Maple Glen": city=1664
if city=="Mapleton": city=1665
if city=="Maplewood": city=1666
if city=="Marathon": city=1667
if city=="Marble": city=1668
if city=="Marble Canyon": city=1669
if city=="Marblehead": city=1670
if city=="Marbletown": city=1671
if city=="Marcellus": city=1672
if city=="Mardela Springs": city=1673
if city=="Marengo": city=1674
if city=="Marfa": city=1675
if city=="Margaretville": city=1676
if city=="Margate": city=1677
if city=="Maricopa": city=1678
if city=="Marietta": city=1679
if city=="Marina": city=1680
if city=="Marina Del Rey": city=1681
if city=="Marine On St Croix": city=1682
if city=="Marion": city=1683
if city=="Markle": city=1684
if city=="Marlboro": city=1685
if city=="Marlborough": city=1686
if city=="Marlin": city=1687
if city=="Marlton": city=1688
if city=="Marquette": city=1689
if city=="Mars": city=1690
if city=="Mars Hill": city=1691
if city=="Marshall": city=1692
if city=="Martin": city=1693
if city=="Martinez": city=1694
if city=="Martins Ferry": city=1695
if city=="Martinsburg": city=1696
if city=="Martinsville": city=1697
if city=="Marysville": city=1698
if city=="Maryville": city=1699
if city=="Mashpee": city=1700
if city=="Mason": city=1701
if city=="Mason City": city=1702
if city=="Massapequa": city=1703
if city=="Massillon": city=1704
if city=="Mastic": city=1705
if city=="Mastic Beach": city=1706
if city=="Matawan": city=1707
if city=="Matthews": city=1708
if city=="Mayer": city=1709
if city=="Maynard": city=1710
if city=="Mays Landing": city=1711
if city=="Maysville": city=1712
if city=="Maywood": city=1713
if city=="Mazomanie": city=1714
if city=="Mc Allen": city=1715
if city=="Mc Donough": city=1716
if city=="Mc Henry": city=1717
if city=="Mc Keesport": city=1718
if city=="Mc Kinney": city=1719
if city=="Mc Minnville": city=1720
if city=="Meadow Bridge": city=1721
if city=="Meadville": city=1722
if city=="Mebane": city=1723
if city=="Mechanicsburg": city=1724
if city=="Mechanicsville": city=1725
if city=="Medfield": city=1726
if city=="Medford": city=1727
if city=="Media": city=1728
if city=="Medicine Lake": city=1729
if city=="Medway": city=1730
if city=="Melbourne": city=1731
if city=="Melissa": city=1732
if city=="Memphis": city=1733
if city=="Menahga": city=1734
if city=="Menasha": city=1735
if city=="Mendham": city=1736
if city=="Mendham Township": city=1737
if city=="Mendocino": city=1738
if city=="Menlo Park": city=1739
if city=="Menomonie": city=1740
if city=="Mentor": city=1741
if city=="Mequon": city=1742
if city=="Merced": city=1743
if city=="Mercer Island": city=1744
if city=="Meredith": city=1745
if city=="Meriden": city=1746
if city=="Meridian": city=1747
if city=="Merrill": city=1748
if city=="Merrillville": city=1749
if city=="Merrimack": city=1750
if city=="Merritt Island": city=1751
if city=="Mesa": city=1752
if city=="Mesick": city=1753
if city=="Mesquite": city=1754
if city=="Metairie": city=1755
if city=="Methuen": city=1756
if city=="Metuchen": city=1757
if city=="Miami": city=1758
if city=="Miami Beach": city=1759
if city=="Miami Gardens": city=1760
if city=="Miami Lakes": city=1761
if city=="Michiana": city=1762
if city=="Michigan City": city=1763
if city=="Middlebury": city=1764
if city=="Middlefield": city=1765
if city=="Middleport": city=1766
if city=="Middlesex": city=1767
if city=="Middletown": city=1768
if city=="Midland": city=1769
if city=="Midlothian": city=1770
if city=="Midway": city=1771
if city=="Midwest": city=1772
if city=="Midwest City": city=1773
if city=="Milbridge": city=1774
if city=="Milford": city=1775
if city=="Mill Creek": city=1776
if city=="Mill Valley": city=1777
if city=="Millbrae": city=1778
if city=="Milledgeville": city=1779
if city=="Millersville": city=1780
if city=="Millerton": city=1781
if city=="Millis": city=1782
if city=="Millville": city=1783
if city=="Milo": city=1784
if city=="Milpitas": city=1785
if city=="Milton": city=1786
if city=="Milwaukee": city=1787
if city=="Milwaukie": city=1788
if city=="Minden": city=1789
if city=="Mineral": city=1790
if city=="Minneapolis": city=1791
if city=="Minnesota Lake": city=1792
if city=="Minnetonka": city=1793
if city=="Minot": city=1794
if city=="Mint Hill": city=1795
if city=="Miramar": city=1796
if city=="Mishawaka": city=1797
if city=="Miss State": city=1798
if city=="Mission": city=1799
if city=="Mission Viejo": city=1800
if city=="Missoula": city=1801
if city=="Mitchell": city=1802
if city=="Moab": city=1803
if city=="Mobile": city=1804
if city=="Mocksville": city=1805
if city=="Modesto": city=1806
if city=="Mohawk": city=1807
if city=="Mojave": city=1808
if city=="Molalla": city=1809
if city=="Moline": city=1810
if city=="Moncks Corner": city=1811
if city=="Monhegan": city=1812
if city=="Monroe": city=1813
if city=="Monroe Township": city=1814
if city=="Monsey": city=1815
if city=="Montauk": city=1816
if city=="Montclair": city=1817
if city=="Montebello": city=1818
if city=="Montegut": city=1819
if city=="Monterey": city=1820
if city=="Montesano": city=1821
if city=="Montgomery": city=1822
if city=="Montgomery Village": city=1823
if city=="Montpelier": city=1824
if city=="Montrose": city=1825
if city=="Montville": city=1826
if city=="Moorestown": city=1827
if city=="Mooresville": city=1828
if city=="Moorhead": city=1829
if city=="Moorpark": city=1830
if city=="Mora": city=1831
if city=="Moraga": city=1832
if city=="Moraine": city=1833
if city=="Morehead": city=1834
if city=="Moreno Valley": city=1835
if city=="Morgan Hill": city=1836
if city=="Morganton": city=1837
if city=="Morgantown": city=1838
if city=="Morris": city=1839
if city=="Morristown": city=1840
if city=="Morrisville": city=1841
if city=="Morro Bay": city=1842
if city=="Moscow": city=1843
if city=="Moses Lake": city=1844
if city=="Moss Landing": city=1845
if city=="Moultrie": city=1846
if city=="Mound Bayou": city=1847
if city=="Mount Pleasant": city=1848
if city=="Mount Shasta": city=1849
if city=="Mount Vernon": city=1850
if city=="Mountain Home": city=1851
if city=="Mountain View": city=1852
if city=="Mountlake Terrace": city=1853
if city=="Mt Airy": city=1854
if city=="Mt Baldy": city=1855
if city=="Mt Desert": city=1856
if city=="Mt Gilead": city=1857
if city=="Mt Holly": city=1858
if city=="Mt Joy": city=1859
if city=="Mt Juliet": city=1860
if city=="Mt Pleasant": city=1861
if city=="Mt Sterling": city=1862
if city=="Mt Vernon": city=1863
if city=="Mukwonago": city=1864
if city=="Mulberry": city=1865
if city=="Mullica Hill": city=1866
if city=="Muncie": city=1867
if city=="Muncy": city=1868
if city=="Mundelein": city=1869
if city=="Munnsville": city=1870
if city=="Munster": city=1871
if city=="Murfreesboro": city=1872
if city=="Murphys": city=1873
if city=="Murray": city=1874
if city=="Murrieta": city=1875
if city=="Muscatine": city=1876
if city=="Muscle Shoals": city=1877
if city=="Muskegon": city=1878
if city=="Muskogee": city=1879
if city=="Mustang": city=1880
if city=="Mutual": city=1881
if city=="Myrtle Beach": city=1882
if city=="Myrtle Creek": city=1883
if city=="Mystic": city=1884
if city=="Naalehu": city=1885
if city=="Nacogdoches": city=1886
if city=="Nampa": city=1887
if city=="Nanticoke": city=1888
if city=="Nantucket": city=1889
if city=="Nanuet": city=1890
if city=="Napa": city=1891
if city=="Naperville": city=1892
if city=="Naples": city=1893
if city=="Napoleon": city=1894
if city=="Narragansett": city=1895
if city=="Nashua": city=1896
if city=="Nashville": city=1897
if city=="Nashville Davidson (Balance)": city=1898
if city=="National Park": city=1899
if city=="Naturita": city=1900
if city=="Naugatuck": city=1901
if city=="Neah Bay": city=1902
if city=="Neche": city=1903
if city=="Nederland": city=1904
if city=="Needham": city=1905
if city=="Neenah": city=1906
if city=="Nelson": city=1907
if city=="Neosho": city=1908
if city=="Neptune City": city=1909
if city=="Neskowin": city=1910
if city=="Netcong": city=1911
if city=="Nevada City": city=1912
if city=="New": city=1913
if city=="New Albany": city=1914
if city=="New Bedford": city=1915
if city=="New Bern": city=1916
if city=="New Braunfels": city=1917
if city=="New Britain": city=1918
if city=="New Brunswick": city=1919
if city=="New Canaan": city=1920
if city=="New Castle": city=1921
if city=="New City": city=1922
if city=="New Concord": city=1923
if city=="New Cumberland": city=1924
if city=="New Hampton": city=1925
if city=="New Harmony": city=1926
if city=="New Hartford": city=1927
if city=="New Haven": city=1928
if city=="New Hope": city=1929
if city=="New Iberia": city=1930
if city=="New Leipzig": city=1931
if city=="New Lenox": city=1932
if city=="New Lexington": city=1933
if city=="New London": city=1934
if city=="New Milford": city=1935
if city=="New Orleans": city=1936
if city=="New Oxford": city=1937
if city=="New Paltz": city=1938
if city=="New Philadelphia": city=1939
if city=="New Port Richey": city=1940
if city=="New Providence": city=1941
if city=="New Richmond": city=1942
if city=="New Rochelle": city=1943
if city=="New Sharon": city=1944
if city=="New Smyrna Beach": city=1945
if city=="New Town": city=1946
if city=="New Wilmington": city=1947
if city=="New York": city=1948
if city=="Newark": city=1949
if city=="Newaygo": city=1950
if city=="Newberg": city=1951
if city=="Newberry": city=1952
if city=="Newburgh": city=1953
if city=="Newbury": city=1954
if city=="Newbury Park": city=1955
if city=="Newcastle": city=1956
if city=="Newfane": city=1957
if city=="Newfield": city=1958
if city=="Newhall": city=1959
if city=="Newington": city=1960
if city=="Newman": city=1961
if city=="Newmarket": city=1962
if city=="Newnan": city=1963
if city=="Newport": city=1964
if city=="Newport Beach": city=1965
if city=="Newport News": city=1966
if city=="Newton": city=1967
if city=="Newtown": city=1968
if city=="Newtown Square": city=1969
if city=="Niagara Falls": city=1970
if city=="Nicasio": city=1971
if city=="Niceville": city=1972
if city=="Niland": city=1973
if city=="Niles": city=1974
if city=="Niskayuna": city=1975
if city=="Nixa": city=1976
if city=="Noble": city=1977
if city=="Noblesville": city=1978
if city=="Nogales": city=1979
if city=="Nome": city=1980
if city=="Norcross": city=1981
if city=="Norfolk": city=1982
if city=="Normal": city=1983
if city=="Norman": city=1984
if city=="North": city=1985
if city=="North Adams": city=1986
if city=="North Andover": city=1987
if city=="North Antelope Valley": city=1988
if city=="North Attleboro": city=1989
if city=="North Augusta": city=1990
if city=="North Bend": city=1991
if city=="North Bergen": city=1992
if city=="North Bethesda": city=1993
if city=="North Brunswick Township": city=1994
if city=="North Canton": city=1995
if city=="North Charleston": city=1996
if city=="North Creek": city=1997
if city=="North East": city=1998
if city=="North Hanover": city=1999
if city=="North Hollywood": city=2000
if city=="North Kingstown": city=2001
if city=="North Las Vegas": city=2002
if city=="North Lewisburg": city=2003
if city=="North Little Rock": city=2004
if city=="North Myrtle Beach": city=2005
if city=="North Platte": city=2006
if city=="North Pole": city=2007
if city=="North Port": city=2008
if city=="North Providence": city=2009
if city=="North Redington Beach": city=2010
if city=="North Royalton": city=2011
if city=="North Smithfield": city=2012
if city=="North Springfield": city=2013
if city=="North Versailles": city=2014
if city=="North Wildwood": city=2015
if city=="Northampton": city=2016
if city=="Northern": city=2017
if city=="Northfield": city=2018
if city=="Northport": city=2019
if city=="Northridge": city=2020
if city=="Northwest": city=2021
if city=="Northwest Josephine": city=2022
if city=="Northwood": city=2023
if city=="Norton": city=2024
if city=="Norwalk": city=2025
if city=="Norwich": city=2026
if city=="Norwood": city=2027
if city=="Novato": city=2028
if city=="Novi": city=2029
if city=="Nucla": city=2030
if city=="Nutley": city=2031
if city=="Nyack": city=2032
if city=="Nyssa": city=2033
if city=="Oak Bluffs": city=2034
if city=="Oak Creek": city=2035
if city=="Oak Harbor": city=2036
if city=="Oak Park": city=2037
if city=="Oak Ridge": city=2038
if city=="Oakdale": city=2039
if city=="Oakhurst": city=2040
if city=="Oakland": city=2041
if city=="Oakley": city=2042
if city=="Oaklyn": city=2043
if city=="Oakton": city=2044
if city=="Oberlin": city=2045
if city=="Ocala": city=2046
if city=="Occidental": city=2047
if city=="Ocean City": city=2048
if city=="Ocean Grove": city=2049
if city=="Ocean Springs": city=2050
if city=="Oceanside": city=2051
if city=="Oconomowoc": city=2052
if city=="Odenton": city=2053
if city=="Odessa": city=2054
if city=="Ogden": city=2055
if city=="Ohio": city=2056
if city=="Ohio City": city=2057
if city=="Ojai": city=2058
if city=="Oklahoma City": city=2059
if city=="Olalla": city=2060
if city=="Olathe": city=2061
if city=="Old Bridge": city=2062
if city=="Old Fort": city=2063
if city=="Old Lyme": city=2064
if city=="Old Saybrook": city=2065
if city=="Oldsmar": city=2066
if city=="Olive Branch": city=2067
if city=="Oliver": city=2068
if city=="Olivet": city=2069
if city=="Olney": city=2070
if city=="Olympia": city=2071
if city=="Olympia Fields": city=2072
if city=="Omaha": city=2073
if city=="Oneonta": city=2074
if city=="Oneota": city=2075
if city=="Ontario": city=2076
if city=="Orange": city=2077
if city=="Orange Park": city=2078
if city=="Orangeburg": city=2079
if city=="Orcas": city=2080
if city=="Oregon": city=2081
if city=="Oregon City": city=2082
if city=="Orem": city=2083
if city=="Orion": city=2084
if city=="Orlando": city=2085
if city=="Orleans": city=2086
if city=="Ormond Beach": city=2087
if city=="Orono": city=2088
if city=="Oroville": city=2089
if city=="Orrville": city=2090
if city=="Osage Beach": city=2091
if city=="Osceola": city=2092
if city=="Oshkosh": city=2093
if city=="Ossining": city=2094
if city=="Oswego": city=2095
if city=="Otis": city=2096
if city=="Otsego": city=2097
if city=="Ottawa": city=2098
if city=="Ottumwa": city=2099
if city=="Oulu": city=2100
if city=="Overland Park": city=2101
if city=="Oviedo": city=2102
if city=="Owatonna": city=2103
if city=="Owensville": city=2104
if city=="Owings Mills": city=2105
if city=="Owosso": city=2106
if city=="Oxford": city=2107
if city=="Oxnard": city=2108
if city=="Oxon Hill": city=2109
if city=="Oyster Bay": city=2110
if city=="Pacific City": city=2111
if city=="Pacific Grove": city=2112
if city=="Pacifica": city=2113
if city=="Paducah": city=2114
if city=="Page": city=2115
if city=="Pagosa Springs": city=2116
if city=="Paguate": city=2117
if city=="Paia": city=2118
if city=="Paintsville": city=2119
if city=="Palenville": city=2120
if city=="Palestine": city=2121
if city=="Palm Bay": city=2122
if city=="Palm Beach": city=2123
if city=="Palm Coast": city=2124
if city=="Palm Desert": city=2125
if city=="Palm Harbor": city=2126
if city=="Palm Springs": city=2127
if city=="Palmdale": city=2128
if city=="Palmetto": city=2129
if city=="Palmyra": city=2130
if city=="Palo Alto": city=2131
if city=="Palos Verdes Estates": city=2132
if city=="Panama City": city=2133
if city=="Panama City Beach": city=2134
if city=="Panhandle": city=2135
if city=="Paonia": city=2136
if city=="Papaikou": city=2137
if city=="Paramus": city=2138
if city=="Paris": city=2139
if city=="Parish": city=2140
if city=="Park City": city=2141
if city=="Park Rapids": city=2142
if city=="Park Slope": city=2143
if city=="Parker": city=2144
if city=="Parkersburg": city=2145
if city=="Parksley": city=2146
if city=="Parma": city=2147
if city=="Parsippany": city=2148
if city=="Parsons": city=2149
if city=="Pasadena": city=2150
if city=="Pasco": city=2151
if city=="Paso Robles": city=2152
if city=="Patagonia": city=2153
if city=="Patchogue": city=2154
if city=="Paterson": city=2155
if city=="Paulsboro": city=2156
if city=="Paw Paw": city=2157
if city=="Pawnee": city=2158
if city=="Pawtucket": city=2159
if city=="Payette": city=2160
if city=="Payson": city=2161
if city=="Peabody": city=2162
if city=="Peaks": city=2163
if city=="Pearl City": city=2164
if city=="Pearl Harbor": city=2165
if city=="Pearl River": city=2166
if city=="Pearland": city=2167
if city=="Pearlington": city=2168
if city=="Pecos": city=2169
if city=="Peekskill": city=2170
if city=="Pelham": city=2171
if city=="Pell City": city=2172
if city=="Pembroke Pines": city=2173
if city=="Pen Argyl": city=2174
if city=="Pendleton": city=2175
if city=="Penndel": city=2176
if city=="Pennington": city=2177
if city=="Pennsauken": city=2178
if city=="Pensacola": city=2179
if city=="Peoria": city=2180
if city=="Peoria Heights": city=2181
if city=="Pepin": city=2182
if city=="Perkasie": city=2183
if city=="Perris": city=2184
if city=="Peru": city=2185
if city=="Pescadero": city=2186
if city=="Petaluma": city=2187
if city=="Peterborough": city=2188
if city=="Peterson": city=2189
if city=="Petoskey": city=2190
if city=="Phenix City": city=2191
if city=="Philadelphia": city=2192
if city=="Philipsburg": city=2193
if city=="Phillipsburg": city=2194
if city=="Phoenix": city=2195
if city=="Phoenixville": city=2196
if city=="Pickens": city=2197
if city=="Piedmont": city=2198
if city=="Piermont": city=2199
if city=="Pierre": city=2200
if city=="Pigeon Forge": city=2201
if city=="Pikeville": city=2202
if city=="Pilot Mountain": city=2203
if city=="Pilot Point": city=2204
if city=="Pinckney": city=2205
if city=="Pine Bluff": city=2206
if city=="Pine Plains": city=2207
if city=="Pine Ridge": city=2208
if city=="Pinellas Park": city=2209
if city=="Pinetop": city=2210
if city=="Pinole": city=2211
if city=="Piscataway": city=2212
if city=="Pismo Beach": city=2213
if city=="Pittsboro": city=2214
if city=="Pittsburg": city=2215
if city=="Pittsburgh": city=2216
if city=="Pittsfield": city=2217
if city=="Pittston": city=2218
if city=="Placentia": city=2219
if city=="Placerville": city=2220
if city=="Plainfield": city=2221
if city=="Plainsboro": city=2222
if city=="Plainville": city=2223
if city=="Plano": city=2224
if city=="Plant City": city=2225
if city=="Plattsburgh": city=2226
if city=="Pleasant Garden": city=2227
if city=="Pleasant Grove": city=2228
if city=="Pleasant Hill": city=2229
if city=="Pleasant Valley": city=2230
if city=="Pleasant View": city=2231
if city=="Pleasanton": city=2232
if city=="Pleasantville": city=2233
if city=="Plymouth": city=2234
if city=="Pocatello": city=2235
if city=="Pocono": city=2236
if city=="Podunk": city=2237
if city=="Point Of Rocks": city=2238
if city=="Point Pleasant": city=2239
if city=="Point Pleasant Beach": city=2240
if city=="Point Reyes Sta": city=2241
if city=="Poland": city=2242
if city=="Pomfret": city=2243
if city=="Pomona": city=2244
if city=="Pompano Beach": city=2245
if city=="Ponce De Leon": city=2246
if city=="Ponder": city=2247
if city=="Pontiac": city=2248
if city=="Poplarville": city=2249
if city=="Port Angeles": city=2250
if city=="Port Arthur": city=2251
if city=="Port Charlotte": city=2252
if city=="Port Chester": city=2253
if city=="Port Clinton": city=2254
if city=="Port Ewen": city=2255
if city=="Port Gibson": city=2256
if city=="Port Huron": city=2257
if city=="Port Jefferson": city=2258
if city=="Port Norris": city=2259
if city=="Port Orchard": city=2260
if city=="Port Orford": city=2261
if city=="Port Richey": city=2262
if city=="Port Salerno": city=2263
if city=="Port St Lucie": city=2264
if city=="Port Sulphur": city=2265
if city=="Port Townsend": city=2266
if city=="Portales": city=2267
if city=="Porterville": city=2268
if city=="Portland": city=2269
if city=="Portola Valley": city=2270
if city=="Portsmouth": city=2271
if city=="Posen": city=2272
if city=="Potsdam": city=2273
if city=="Pottsville": city=2274
if city=="Poughkeepsie": city=2275
if city=="Poulsbo": city=2276
if city=="Poultney": city=2277
if city=="Pound Ridge": city=2278
if city=="Poway": city=2279
if city=="Powder River": city=2280
if city=="Powder Springs": city=2281
if city=="Powhatan": city=2282
if city=="Prairie Village": city=2283
if city=="Prattville": city=2284
if city=="Prescott": city=2285
if city=="Prescott Valley": city=2286
if city=="Presque Isle": city=2287
if city=="Princeton": city=2288
if city=="Providence": city=2289
if city=="Provincetown": city=2290
if city=="Provo": city=2291
if city=="Prudhoe Bay": city=2292
if city=="Prunedale": city=2293
if city=="Pueblo": city=2294
if city=="Pueblo West": city=2295
if city=="Pukalani": city=2296
if city=="Pulaski": city=2297
if city=="Pullman": city=2298
if city=="Punta Gorda": city=2299
if city=="Purcellville": city=2300
if city=="Purchase": city=2301
if city=="Putnam": city=2302
if city=="Putney": city=2303
if city=="Puyallup": city=2304
if city=="P’ÜÎhoa": city=2305
if city=="Quaker City": city=2306
if city=="Quakertown": city=2307
if city=="Quantico": city=2308
if city=="Queen Creek": city=2309
if city=="Queens": city=2310
if city=="Queensbury": city=2311
if city=="Questa": city=2312
if city=="Quilcene": city=2313
if city=="Quincy": city=2314
if city=="Quitman": city=2315
if city=="Quoddy": city=2316
if city=="Racine": city=2317
if city=="Radcliff": city=2318
if city=="Radford": city=2319
if city=="Rahway": city=2320
if city=="Raleigh": city=2321
if city=="Rancho Cucamonga": city=2322
if city=="Rancho Palos Verdes": city=2323
if city=="Rancho Santa Margarita": city=2324
if city=="Randolph": city=2325
if city=="Rangeley": city=2326
if city=="Rapid City": city=2327
if city=="Ray": city=2328
if city=="Raymond": city=2329
if city=="Reading": city=2330
if city=="Red Bank": city=2331
if city=="Red Feather Lakes": city=2332
if city=="Red Hook": city=2333
if city=="Red Oak": city=2334
if city=="Redding": city=2335
if city=="Redford": city=2336
if city=="Redkey": city=2337
if city=="Redlands": city=2338
if city=="Redmond": city=2339
if city=="Redondo Beach": city=2340
if city=="Redway": city=2341
if city=="Redwood": city=2342
if city=="Redwood City": city=2343
if city=="Redwood Valley": city=2344
if city=="Reedsport": city=2345
if city=="Rehoboth": city=2346
if city=="Reno": city=2347
if city=="Rensselaer": city=2348
if city=="Renton": city=2349
if city=="Revere": city=2350
if city=="Rexburg": city=2351
if city=="Rhinelander": city=2352
if city=="Rialto": city=2353
if city=="Rice Lake": city=2354
if city=="Richfield": city=2355
if city=="Richland": city=2356
if city=="Richlands": city=2357
if city=="Richmond": city=2358
if city=="Richwood": city=2359
if city=="Ridge": city=2360
if city=="Ridge Spring": city=2361
if city=="Ridgecrest": city=2362
if city=="Ridgefield": city=2363
if city=="Ridgeland": city=2364
if city=="Ridgewood": city=2365
if city=="Riegelsville": city=2366
if city=="Rimrock": city=2367
if city=="Ringgold": city=2368
if city=="Ringwood": city=2369
if city=="Rio Rancho": city=2370
if city=="Ripley": city=2371
if city=="River Falls": city=2372
if city=="River Vale": city=2373
if city=="Riverbank": city=2374
if city=="Riverside": city=2375
if city=="Riverton": city=2376
if city=="Roanoke": city=2377
if city=="Roaring River": city=2378
if city=="Robbinsville": city=2379
if city=="Rochester": city=2380
if city=="Rochester Hills": city=2381
if city=="Rock Hill": city=2382
if city=="Rock Island": city=2383
if city=="Rock Rapids": city=2384
if city=="Rockaway": city=2385
if city=="Rockford": city=2386
if city=="Rockland": city=2387
if city=="Rockledge": city=2388
if city=="Rocklin": city=2389
if city=="Rockport": city=2390
if city=="Rockville": city=2391
if city=="Rockville Centre": city=2392
if city=="Rocky Mt": city=2393
if city=="Rocky Point": city=2394
if city=="Rogers": city=2395
if city=="Rohnert Park": city=2396
if city=="Rollinsford": city=2397
if city=="Rome": city=2398
if city=="Rome City": city=2399
if city=="Romulus": city=2400
if city=="Ronkonkoma": city=2401
if city=="Roscommon": city=2402
if city=="Roseburg": city=2403
if city=="Rosendale": city=2404
if city=="Roseto": city=2405
if city=="Roseville": city=2406
if city=="Roslyn": city=2407
if city=="Roswell": city=2408
if city=="Rotterdam": city=2409
if city=="Round Lake": city=2410
if city=="Round Rock": city=2411
if city=="Rowlett": city=2412
if city=="Rowley": city=2413
if city=="Roxbury": city=2414
if city=="Royal Oak": city=2415
if city=="Royersford": city=2416
if city=="Ruby": city=2417
if city=="Ruidoso": city=2418
if city=="Rumford": city=2419
if city=="Rumson": city=2420
if city=="Running Springs": city=2421
if city=="Russell": city=2422
if city=="Russellville": city=2423
if city=="Russian Mission": city=2424
if city=="Ruston": city=2425
if city=="Rutherford": city=2426
if city=="Rutherfordton": city=2427
if city=="Rutland": city=2428
if city=="Sabillasville": city=2429
if city=="Sachse": city=2430
if city=="Saco": city=2431
if city=="Sacramento": city=2432
if city=="Safety Harbor": city=2433
if city=="Sag Harbor": city=2434
if city=="Saginaw": city=2435
if city=="Sahuarita": city=2436
if city=="Saint Cloud": city=2437
if city=="Saint Helena": city=2438
if city=="Saint James": city=2439
if city=="Salamanca": city=2440
if city=="Salem": city=2441
if city=="Salina": city=2442
if city=="Salinas": city=2443
if city=="Salisbury": city=2444
if city=="Sallisaw": city=2445
if city=="Salt Lake City": city=2446
if city=="Salt Lick": city=2447
if city=="Saltsburg": city=2448
if city=="Saluda": city=2449
if city=="Sammamish": city=2450
if city=="Samnorwood": city=2451
if city=="San Angelo": city=2452
if city=="San Anselmo": city=2453
if city=="San Antonio": city=2454
if city=="San Bernardino": city=2455
if city=="San Bruno": city=2456
if city=="San Buenaventura (Ventura)": city=2457
if city=="San Carlos": city=2458
if city=="San Clemente": city=2459
if city=="San Diego": city=2460
if city=="San Fernando": city=2461
if city=="San Fernando Valley": city=2462
if city=="San Francisco": city=2463
if city=="San Gabriel": city=2464
if city=="San Jacinto": city=2465
if city=="San Jose": city=2466
if city=="San Juan Capistrano": city=2467
if city=="San Leandro": city=2468
if city=="San Luis Obispo": city=2469
if city=="San Marcos": city=2470
if city=="San Mateo": city=2471
if city=="San Pablo": city=2472
if city=="San Pedro": city=2473
if city=="San Rafael": city=2474
if city=="San Ramon": city=2475
if city=="Sand Point": city=2476
if city=="Sandpoint": city=2477
if city=="Sandusky": city=2478
if city=="Sandwich": city=2479
if city=="Sandy": city=2480
if city=="Sandy Hook": city=2481
if city=="Sandy Springs": city=2482
if city=="Sanford": city=2483
if city=="Sanibel": city=2484
if city=="Santa Ana": city=2485
if city=="Santa Barbara": city=2486
if city=="Santa Clara": city=2487
if city=="Santa Clarita": city=2488
if city=="Santa Cruz": city=2489
if city=="Santa Fe": city=2490
if city=="Santa Maria": city=2491
if city=="Santa Monica": city=2492
if city=="Santa Nella Village": city=2493
if city=="Santa Paula": city=2494
if city=="Santa Rosa": city=2495
if city=="Santa Ynez Valley": city=2496
if city=="Santee": city=2497
if city=="Saranac": city=2498
if city=="Saranac Lake": city=2499
if city=="Sarasota": city=2500
if city=="Saratoga Springs": city=2501
if city=="Saugerties": city=2502
if city=="Sauk City": city=2503
if city=="Sauk Rapids": city=2504
if city=="Saukville": city=2505
if city=="Sausalito": city=2506
if city=="Savage": city=2507
if city=="Savannah": city=2508
if city=="Savoy": city=2509
if city=="Saxapahaw": city=2510
if city=="Sayreville": city=2511
if city=="Sayville": city=2512
if city=="Scarborough": city=2513
if city=="Scarsdale": city=2514
if city=="Schaumburg": city=2515
if city=="Schenectady": city=2516
if city=="Schwenksville": city=2517
if city=="Scituate": city=2518
if city=="Scotch Plains": city=2519
if city=="Scotia": city=2520
if city=="Scott": city=2521
if city=="Scott City": city=2522
if city=="Scottsbluff": city=2523
if city=="Scottsdale": city=2524
if city=="Scranton": city=2525
if city=="Sea Ranch": city=2526
if city=="Seabrook": city=2527
if city=="Seaford": city=2528
if city=="Seagrove": city=2529
if city=="Seal Beach": city=2530
if city=="Seaside": city=2531
if city=="Seattle": city=2532
if city=="Sebastopol": city=2533
if city=="Secaucus": city=2534
if city=="Sedona": city=2535
if city=="Seffner": city=2536
if city=="Sellersburg": city=2537
if city=="Sells": city=2538
if city=="Selmer": city=2539
if city=="Seminole": city=2540
if city=="Seneca": city=2541
if city=="Sequim": city=2542
if city=="Sequoia National Park": city=2543
if city=="Sergeant Bluff": city=2544
if city=="Severn": city=2545
if city=="Severna Park": city=2546
if city=="Seville": city=2547
if city=="Sewaren": city=2548
if city=="Shade Gap": city=2549
if city=="Shafer": city=2550
if city=="Shaker Heights": city=2551
if city=="Shakopee": city=2552
if city=="Shandaken": city=2553
if city=="Sharon": city=2554
if city=="Shawnee": city=2555
if city=="Sheboygan Falls": city=2556
if city=="Sheffield": city=2557
if city=="Shelburne": city=2558
if city=="Shelburne Falls": city=2559
if city=="Shelby": city=2560
if city=="Shelbyville": city=2561
if city=="Shell Lake": city=2562
if city=="Shelter Island": city=2563
if city=="Shelton": city=2564
if city=="Shenandoah": city=2565
if city=="Shepherd": city=2566
if city=="Sherman": city=2567
if city=="Sherman Oaks": city=2568
if city=="Sherwood": city=2569
if city=="Ship Bottom": city=2570
if city=="Shippensburg": city=2571
if city=="Shiprock": city=2572
if city=="Shoreham": city=2573
if city=="Shoreline": city=2574
if city=="Shoreview": city=2575
if city=="Short Hills": city=2576
if city=="Show Low": city=2577
if city=="Shreveport": city=2578
if city=="Shrewsbury": city=2579
if city=="Sicklerville": city=2580
if city=="Sidney": city=2581
if city=="Sierra Blanca": city=2582
if city=="Sierra Madre": city=2583
if city=="Sierra Vista": city=2584
if city=="Signal Hill": city=2585
if city=="Siler City": city=2586
if city=="Siloam Springs": city=2587
if city=="Silver Lake": city=2588
if city=="Silver Spring": city=2589
if city=="Silverado": city=2590
if city=="Silverton": city=2591
if city=="Simi Valley": city=2592
if city=="Simpsonville": city=2593
if city=="Simsboro": city=2594
if city=="Simsbury Center": city=2595
if city=="Sioux City": city=2596
if city=="Sioux Falls": city=2597
if city=="Sisters": city=2598
if city=="Sitka": city=2599
if city=="Skandia": city=2600
if city=="Skokie": city=2601
if city=="Skowhegan": city=2602
if city=="Slidell": city=2603
if city=="Slippery Rock": city=2604
if city=="Smithfield": city=2605
if city=="Smithtown": city=2606
if city=="Smithville": city=2607
if city=="Smyrna": city=2608
if city=="Snellville": city=2609
if city=="Snohomish": city=2610
if city=="Snowmass": city=2611
if city=="Socorro": city=2612
if city=="Soho": city=2613
if city=="Soldotna": city=2614
if city=="Somers": city=2615
if city=="Somers Point": city=2616
if city=="Somerset": city=2617
if city=="Somersworth": city=2618
if city=="Somerville": city=2619
if city=="Sonoma": city=2620
if city=="Sonora": city=2621
if city=="Soquel": city=2622
if city=="South Amherst": city=2623
if city=="South Beach": city=2624
if city=="South Bend": city=2625
if city=="South Berwick": city=2626
if city=="South Boston": city=2627
if city=="South Bound Brook": city=2628
if city=="South Dennis": city=2629
if city=="South Elgin": city=2630
if city=="South Eliot": city=2631
if city=="South Hill": city=2632
if city=="South Jordan": city=2633
if city=="South Kingstown": city=2634
if city=="South Lake Tahoe": city=2635
if city=="South Orange": city=2636
if city=="South Pasadena": city=2637
if city=="South Portland": city=2638
if city=="South Salem": city=2639
if city=="South San Francisco": city=2640
if city=="South Woodbury": city=2641
if city=="Southampton": city=2642
if city=="Southern": city=2643
if city=="Southern Pines": city=2644
if city=="Southern Shores": city=2645
if city=="Southgate": city=2646
if city=="Southington": city=2647
if city=="Southold": city=2648
if city=="Southport": city=2649
if city=="Southwest": city=2650
if city=="Southwest Meade": city=2651
if city=="Spanish Fork": city=2652
if city=="Sparks": city=2653
if city=="Sparta": city=2654
if city=="Spartanburg": city=2655
if city=="Spencer": city=2656
if city=="Spokane": city=2657
if city=="Spokane Valley": city=2658
if city=="Spotswood": city=2659
if city=="Sprague": city=2660
if city=="Spring": city=2661
if city=="Spring Lake": city=2662
if city=="Spring Valley": city=2663
if city=="Springfield": city=2664
if city=="Springtown": city=2665
if city=="Springville": city=2666
if city=="Squaw Valley": city=2667
if city=="St Albans": city=2668
if city=="St Augustine": city=2669
if city=="St Charles": city=2670
if city=="St Clair": city=2671
if city=="St Clair Shores": city=2672
if city=="St Cloud": city=2673
if city=="St Francisville": city=2674
if city=="St George": city=2675
if city=="St James": city=2676
if city=="St Johns": city=2677
if city=="St Johnsbury": city=2678
if city=="St Joseph": city=2679
if city=="St Louis": city=2680
if city=="St Marys": city=2681
if city=="St Paul": city=2682
if city=="St Pete Beach": city=2683
if city=="St Peter": city=2684
if city=="St Peters": city=2685
if city=="St Petersburg": city=2686
if city=="St Robert": city=2687
if city=="St Simons": city=2688
if city=="St. Joseph": city=2689
if city=="St. Louis Park": city=2690
if city=="Stafford": city=2691
if city=="Stafford Springs": city=2692
if city=="Stamford": city=2693
if city=="Stanford": city=2694
if city=="Stanley": city=2695
if city=="Stanwood": city=2696
if city=="Starksboro": city=2697
if city=="Starkville": city=2698
if city=="State College": city=2699
if city=="Stateline": city=2700
if city=="Staten Island": city=2701
if city=="Statesboro": city=2702
if city=="Statesville": city=2703
if city=="Staunton": city=2704
if city=="Stehekin": city=2705
if city=="Steilacoom": city=2706
if city=="Sterling": city=2707
if city=="Sterling Heights": city=2708
if city=="Steuben": city=2709
if city=="Stevens Point": city=2710
if city=="Stevensville": city=2711
if city=="Stewartstown": city=2712
if city=="Stillwater": city=2713
if city=="Stockbridge": city=2714
if city=="Stockton": city=2715
if city=="Stone Mountain": city=2716
if city=="Stone Ridge": city=2717
if city=="Stonington": city=2718
if city=="Stony Brook": city=2719
if city=="Stony Point": city=2720
if city=="Storm Lake": city=2721
if city=="Stoughton": city=2722
if city=="Stow": city=2723
if city=="Stowe": city=2724
if city=="Stratford": city=2725
if city=="Stroud": city=2726
if city=="Stroudsburg": city=2727
if city=="Studio City": city=2728
if city=="Sturgeon Bay": city=2729
if city=="Sturgis": city=2730
if city=="Succasunna": city=2731
if city=="Suffern": city=2732
if city=="Suffolk": city=2733
if city=="Sugar Hill": city=2734
if city=="Sugar Land": city=2735
if city=="Sulphur": city=2736
if city=="Sulphur Springs": city=2737
if city=="Sultan": city=2738
if city=="Summertown": city=2739
if city=="Summerville": city=2740
if city=="Summit": city=2741
if city=="Sumner": city=2742
if city=="Sumter": city=2743
if city=="Sun City": city=2744
if city=="Sun Prairie": city=2745
if city=="Sunderland": city=2746
if city=="Sunnyside": city=2747
if city=="Sunnyvale": city=2748
if city=="Sunol": city=2749
if city=="Sunrise": city=2750
if city=="Superior": city=2751
if city=="Suquamish": city=2752
if city=="Surprise": city=2753
if city=="Sussex": city=2754
if city=="Sutton": city=2755
if city=="Suwanee": city=2756
if city=="Swampscott": city=2757
if city=="Swansea": city=2758
if city=="Sylva": city=2759
if city=="Sylvan Beach": city=2760
if city=="Syracuse": city=2761
if city=="Tacoma": city=2762
if city=="Taftsville": city=2763
if city=="Tahlequah": city=2764
if city=="Tahoe City": city=2765
if city=="Tahoe Vista": city=2766
if city=="Takoma Park": city=2767
if city=="Talent": city=2768
if city=="Talkeetna": city=2769
if city=="Tallahassee": city=2770
if city=="Tamarac": city=2771
if city=="Tampa": city=2772
if city=="Taos": city=2773
if city=="Tariffville": city=2774
if city=="Tarrytown": city=2775
if city=="Taunton": city=2776
if city=="Taylor": city=2777
if city=="Taylorstown": city=2778
if city=="Tazewell": city=2779
if city=="Teaneck": city=2780
if city=="Tehachapi": city=2781
if city=="Telluride": city=2782
if city=="Temecula": city=2783
if city=="Tempe": city=2784
if city=="Temperance": city=2785
if city=="Temple": city=2786
if city=="Templeton": city=2787
if city=="Tenafly": city=2788
if city=="Terlingua": city=2789
if city=="Terre Haute": city=2790
if city=="Tewksbury": city=2791
if city=="Texarkana": city=2792
if city=="Thayer": city=2793
if city=="The Colony": city=2794
if city=="The Dalles": city=2795
if city=="The Woodlands": city=2796
if city=="Thibodaux": city=2797
if city=="Thomaston": city=2798
if city=="Thomasville": city=2799
if city=="Thompson": city=2800
if city=="Thompsonville": city=2801
if city=="Thornton": city=2802
if city=="Thousand Oaks": city=2803
if city=="Three Rivers": city=2804
if city=="Thurmont": city=2805
if city=="Thurston": city=2806
if city=="Tiburon": city=2807
if city=="Tieton": city=2808
if city=="Tifton": city=2809
if city=="Tigard": city=2810
if city=="Tijeras": city=2811
if city=="Tillamook": city=2812
if city=="Tilton": city=2813
if city=="Tinmouth": city=2814
if city=="Tipton": city=2815
if city=="Titusville": city=2816
if city=="Tivoli": city=2817
if city=="Toledo": city=2818
if city=="Tolland": city=2819
if city=="Tomah": city=2820
if city=="Tomales": city=2821
if city=="Tomball": city=2822
if city=="Tomkins Cove": city=2823
if city=="Toms River": city=2824
if city=="Tonopah": city=2825
if city=="Tooele": city=2826
if city=="Topanga": city=2827
if city=="Topeka": city=2828
if city=="Topsail": city=2829
if city=="Toronto": city=2830
if city=="Torrance": city=2831
if city=="Torrington": city=2832
if city=="Totowa": city=2833
if city=="Townshend": city=2834
if city=="Towson": city=2835
if city=="Trabuco": city=2836
if city=="Tracy": city=2837
if city=="Transylvania": city=2838
if city=="Travelers Rest": city=2839
if city=="Traverse": city=2840
if city=="Traverse City": city=2841
if city=="Trenton": city=2842
if city=="Triangle": city=2843
if city=="Trinity": city=2844
if city=="Troy": city=2845
if city=="Truckee": city=2846
if city=="Trumbull": city=2847
if city=="Truth Or Consequences": city=2848
if city=="Truxton": city=2849
if city=="Tualatin": city=2850
if city=="Tuckahoe": city=2851
if city=="Tucker": city=2852
if city=="Tucson": city=2853
if city=="Tujunga": city=2854
if city=="Tulare": city=2855
if city=="Tulsa": city=2856
if city=="Tunbridge": city=2857
if city=="Tupelo": city=2858
if city=="Turlock": city=2859
if city=="Turner": city=2860
if city=="Turtle Creek": city=2861
if city=="Tuscaloosa": city=2862
if city=="Tuscola": city=2863
if city=="Tustin": city=2864
if city=="Twain Harte": city=2865
if city=="Twentynine Palms": city=2866
if city=="Twentynine Palms Morongo Valley": city=2867
if city=="Twin Falls": city=2868
if city=="Twisp": city=2869
if city=="Two Harbors": city=2870
if city=="Tybee Island": city=2871
if city=="Tyler": city=2872
if city=="Udall": city=2873
if city=="Ukiah": city=2874
if city=="Ulysses": city=2875
if city=="Unalakleet": city=2876
if city=="Union": city=2877
if city=="Union City": city=2878
if city=="Union Grove": city=2879
if city=="Unity": city=2880
if city=="University City": city=2881
if city=="University Park": city=2882
if city=="Upland": city=2883
if city=="Upper Freehold": city=2884
if city=="Upper Marlboro": city=2885
if city=="Upper Pittsgrove": city=2886
if city=="Urbana": city=2887
if city=="Urbandale": city=2888
if city=="Utica": city=2889
if city=="Uxbridge": city=2890
if city=="Vacaville": city=2891
if city=="Vadnais Heights": city=2892
if city=="Vail": city=2893
if city=="Valdosta": city=2894
if city=="Valencia": city=2895
if city=="Vallejo": city=2896
if city=="Valley Cottage": city=2897
if city=="Valparaiso": city=2898
if city=="Valrico": city=2899
if city=="Van Alstyne": city=2900
if city=="Vanceburg": city=2901
if city=="Vancouver": city=2902
if city=="Vanderbilt": city=2903
if city=="Vashon": city=2904
if city=="Venice": city=2905
if city=="Ventnor City": city=2906
if city=="Ventura": city=2907
if city=="Vergennes": city=2908
if city=="Vernon": city=2909
if city=="Vernon Hills": city=2910
if city=="Vero Beach": city=2911
if city=="Verona": city=2912
if city=="Vestal": city=2913
if city=="Vicksburg": city=2914
if city=="Victor": city=2915
if city=="Victorville": city=2916
if city=="Vienna": city=2917
if city=="View Park Windsor Hills": city=2918
if city=="Villa Rica": city=2919
if city=="Village Of Clarkston": city=2920
if city=="Vincennes": city=2921
if city=="Vineland": city=2922
if city=="Vineyard Haven": city=2923
if city=="Virgilina": city=2924
if city=="Virginia Beach": city=2925
if city=="Viroqua": city=2926
if city=="Visalia": city=2927
if city=="Vista": city=2928
if city=="Wabash": city=2929
if city=="Waco": city=2930
if city=="Wadsworth": city=2931
if city=="Wagoner": city=2932
if city=="Waianae": city=2933
if city=="Wailuku": city=2934
if city=="Wainscott": city=2935
if city=="Waitsfield": city=2936
if city=="Wakefield": city=2937
if city=="Wakefield Peacedale": city=2938
if city=="Walden": city=2939
if city=="Waldoboro": city=2940
if city=="Waldorf": city=2941
if city=="Walhalla": city=2942
if city=="Wall Township": city=2943
if city=="Walla Walla": city=2944
if city=="Waller": city=2945
if city=="Wallingford": city=2946
if city=="Walnut": city=2947
if city=="Walnut Creek": city=2948
if city=="Walnut Grove": city=2949
if city=="Walpole": city=2950
if city=="Waltham": city=2951
if city=="Walworth": city=2952
if city=="Wappingers Falls": city=2953
if city=="Ward": city=2954
if city=="Warren": city=2955
if city=="Warrensburg": city=2956
if city=="Warrenton": city=2957
if city=="Warrenville": city=2958
if city=="Warsaw": city=2959
if city=="Wartburg": city=2960
if city=="Warwick": city=2961
if city=="Waseca": city=2962
if city=="Washburn": city=2963
if city=="Washington": city=2964
if city=="Washington Court House": city=2965
if city=="Washington Heights": city=2966
if city=="Washington Island": city=2967
if city=="Washingtonville": city=2968
if city=="Wasilla": city=2969
if city=="Wassaic": city=2970
if city=="Waterbury": city=2971
if city=="Waterford": city=2972
if city=="Waterford Township": city=2973
if city=="Waterloo": city=2974
if city=="Watertown": city=2975
if city=="Waterville": city=2976
if city=="Watkins Glen": city=2977
if city=="Watson": city=2978
if city=="Watsonville": city=2979
if city=="Wauconda": city=2980
if city=="Waukegan": city=2981
if city=="Waukesha": city=2982
if city=="Waunakee": city=2983
if city=="Wausau": city=2984
if city=="Wauwatosa": city=2985
if city=="Waverly": city=2986
if city=="Waverly Hall": city=2987
if city=="Wawayanda": city=2988
if city=="Waxahachie": city=2989
if city=="Waycross": city=2990
if city=="Wayland": city=2991
if city=="Wayne": city=2992
if city=="Waynesboro": city=2993
if city=="Waynesburg": city=2994
if city=="Weare": city=2995
if city=="Weatherford": city=2996
if city=="Weaverville": city=2997
if city=="Webb City": city=2998
if city=="Webster": city=2999
if city=="Weed": city=3000
if city=="Weehawken": city=3001
if city=="Wellesley": city=3002
if city=="Wellfleet": city=3003
if city=="Wellford": city=3004
if city=="Wells": city=3005
if city=="Wellsville": city=3006
if city=="Wenatchee": city=3007
if city=="Wernersville": city=3008
if city=="Wesley Chapel": city=3009
if city=="West": city=3010
if city=="West Babylon": city=3011
if city=="West Bend": city=3012
if city=="West Bloomfield Township": city=3013
if city=="West Branch": city=3014
if city=="West Brookfield": city=3015
if city=="West Chester": city=3016
if city=="West Columbia": city=3017
if city=="West Concord": city=3018
if city=="West Deptford Township": city=3019
if city=="West Des Moines": city=3020
if city=="West Dover": city=3021
if city=="West End": city=3022
if city=="West Fulton": city=3023
if city=="West Grove": city=3024
if city=="West Hartford": city=3025
if city=="West Haven": city=3026
if city=="West Hempstead": city=3027
if city=="West Hills": city=3028
if city=="West Hollywood": city=3029
if city=="West Jordan": city=3030
if city=="West Lafayette": city=3031
if city=="West Long Branch": city=3032
if city=="West Melbourne": city=3033
if city=="West Monroe": city=3034
if city=="West Orange": city=3035
if city=="West Palm Beach": city=3036
if city=="West Plains": city=3037
if city=="West Sacramento": city=3038
if city=="West Shannon": city=3039
if city=="West Stockbridge": city=3040
if city=="West Tisbury": city=3041
if city=="West Topsham": city=3042
if city=="West Warwick": city=3043
if city=="Westbrook": city=3044
if city=="Westby": city=3045
if city=="Westerville": city=3046
if city=="Westfield": city=3047
if city=="Westhampton Beach": city=3048
if city=="Westlake Village": city=3049
if city=="Westland": city=3050
if city=="Westminster": city=3051
if city=="Westmont": city=3052
if city=="Westmoreland": city=3053
if city=="Weston": city=3054
if city=="Westport": city=3055
if city=="Westwood": city=3056
if city=="Wheaton": city=3057
if city=="Wheeling": city=3058
if city=="White House": city=3059
if city=="White Lake": city=3060
if city=="White Plains": city=3061
if city=="White River Junction": city=3062
if city=="White Salmon": city=3063
if city=="White Swan": city=3064
if city=="Whitehall": city=3065
if city=="Whitehouse": city=3066
if city=="Whitehouse Station": city=3067
if city=="Whitewater": city=3068
if city=="Whitmore Lake": city=3069
if city=="Whitsett": city=3070
if city=="Whittier": city=3071
if city=="Wichita": city=3072
if city=="Wilbur": city=3073
if city=="Wildwood": city=3074
if city=="Wilkes Barre": city=3075
if city=="Wilkesboro": city=3076
if city=="Williams": city=3077
if city=="Williamsburg": city=3078
if city=="Williamsport": city=3079
if city=="Williamston": city=3080
if city=="Williamstown": city=3081
if city=="Williamsville": city=3082
if city=="Willingboro": city=3083
if city=="Williston": city=3084
if city=="Willow Grove": city=3085
if city=="Willow River": city=3086
if city=="Willow Springs": city=3087
if city=="Wills Point": city=3088
if city=="Willsboro": city=3089
if city=="Wilmington": city=3090
if city=="Wilmore": city=3091
if city=="Wilsonville": city=3092
if city=="Wilton": city=3093
if city=="Wimberley": city=3094
if city=="Winchester": city=3095
if city=="Windermere": city=3096
if city=="Windsor": city=3097
if city=="Windsor Heights": city=3098
if city=="Winona": city=3099
if city=="Winona Lake": city=3100
if city=="Winslow": city=3101
if city=="Winston Salem": city=3102
if city=="Winter Harbor": city=3103
if city=="Winter Haven": city=3104
if city=="Winter Park": city=3105
if city=="Winters": city=3106
if city=="Winton": city=3107
if city=="Wisconsin Dells": city=3108
if city=="Wise": city=3109
if city=="Wixom": city=3110
if city=="Wolcott": city=3111
if city=="Woodbridge": city=3112
if city=="Woodburn": city=3113
if city=="Woodbury": city=3114
if city=="Woodbury Heights": city=3115
if city=="Woodland": city=3116
if city=="Woodland Park": city=3117
if city=="Woodmere": city=3118
if city=="Woodstock": city=3119
if city=="Woonsocket": city=3120
if city=="Wooster": city=3121
if city=="Worcester": city=3122
if city=="Wrangell": city=3123
if city=="Wyandotte": city=3124
if city=="Wynantskill": city=3125
if city=="Wyoming": city=3126
if city=="Yachats": city=3127
if city=="Yakima": city=3128
if city=="Yankton": city=3129
if city=="Yardley": city=3130
if city=="Yarmouth": city=3131
if city=="Yazoo City": city=3132
if city=="Yellow Springs": city=3133
if city=="Yelm": city=3134
if city=="Yonkers": city=3135
if city=="Yorba Linda": city=3136
if city=="York": city=3137
if city=="Yorktown": city=3138
if city=="Yorktown Heights": city=3139
if city=="Yorkville": city=3140
if city=="Yosemite National Park": city=3141
if city=="Young": city=3142
if city=="Youngstown": city=3143
if city=="Ypsilanti": city=3144
if city=="Yuba City": city=3145
if city=="Yucaipa": city=3146
if city=="Yucca Valley": city=3147
if city=="Yuma": city=3148
if city=="Zanesville": city=3149
if city=="Zephyrhills": city=3150
if city=="Zirconia": city=3151


## Prediction:
prediction = st.sidebar.button("Get Prediction")
if prediction:
	st.markdown("<h1 style='text-align: center; color: SteelBlue;'>KickStarter Prediction Results:</h1>", unsafe_allow_html=True)
	
	print('\n')
	print(cat, sub_cat, city, state, goal, updates, level, duration)

	# if (int(cat) == False or int(sub_cat) ==False or int(city) ==False or int(state) ==False or float(goal) ==False or int(updates) ==False or int(level) ==False or int(duration) ==False):
	# 	st.markdown("<h2 style='text-align: center; color: red;'>Error: All Fields are Required</h2>", unsafe_allow_html=True)
	
	if int(cat) == 10000:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Select valid Category</h2>", unsafe_allow_html=True)

	elif int(sub_cat) == 10000:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Select valid Sub Category Category</h2>", unsafe_allow_html=True)

	elif int(city) == 10000:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Select valid City</h2>", unsafe_allow_html=True)

	elif int(state) == 10000:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Select valid State</h2>", unsafe_allow_html=True)

	elif int(goal) == 0:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Goal cannot be zero</h2>", unsafe_allow_html=True)

	elif int(updates) < 0:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Updates cannot be negative</h2>", unsafe_allow_html=True)

	elif int(level) == 0:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Levels cannot be zero</h2>", unsafe_allow_html=True)

	elif int(level) >15:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Levels cannot be greater than 15</h2>", unsafe_allow_html=True)

	elif int(duration) == 0:
		st.markdown("<h2 style='text-align: center; color: red;'>Error: Project duration cannot be zero</h2>", unsafe_allow_html=True)

	else:
		# email and details
		write_to_disk(name, email)

		data = {'city': [int(city)], 'subcategory': [int(sub_cat)], 'state': [int(state)], 'goal': [float(goal)], 'levels': [int(level)], 'duration': [float(duration)], 'updates': [int(updates)]}
		print(data)
		y_pred = model_run(data)

		# data log
		data_csv = [[title, description, cat, sub_cat, state, city, goal, updates, duration, level, y_pred]]
		with open('data_storage.csv', 'a') as f:
			writer = csv.writer(f)
			writer.writerows(data_csv)
			print('Csv file written')
			f.close()

		if y_pred == 1:
			st.markdown("<h2 style='text-align: center; color: green;'>Congratualtions!</h2>", unsafe_allow_html=True)
			st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'>Looks like the project you are about to start is going be classifed as successful project. This means that the project will get the required funding and backing based on the previous year's data. Go ahead and start a new project. Good Luck with your project.</p>", unsafe_allow_html=True)

		elif y_pred == 0:
			st.markdown("<h2 style='text-align: center; color: red;'>Oops!!</h2>", unsafe_allow_html=True)
			st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'>Looks like the project you are about to start is going be classifed as failed project. This means that, based on your current project details, you will not be getting the required funding and backing based on the previous year's data.</p>", unsafe_allow_html=True)
			st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'><br>Don't Worry, we have a recommendation for you. This recommendation can be useful to get your project suffient backing and funding</br></p>", unsafe_allow_html=True)

			st.markdown("<h2 style='text-align: center; color: Green;'>Our Recommendation:</h2>", unsafe_allow_html=True)
			data = {'city': int(city), 'subcategory': int(sub_cat), 'state': int(state), 'goal': float(goal), 'levels': int(level), 'duration': float(duration), 'updates': int(updates), 'category': int(cat)}
			successful_project,failed_projects,avg_goal,avg_update,avg_duration,avg_level, counter = project_recommendation(data)
			total_projects = successful_project + failed_projects
			print(successful_project,failed_projects,avg_goal,avg_update,avg_duration,avg_level)

			if counter == 0: 
				open_statement = 'Previously, {} projects were posted based on your current selection of Category, Subcategory, State and City. Out of which {} projects were successfull and {} projects were failed.'.format(total_projects, successful_project, failed_projects)
				statement1 = "Based on our recommendation engine's analysis, you can adjust between {} and {}". format(round(avg_goal*0.90,2), round(avg_goal*1.1,2))
				statement2 = "Based on our recommendation engine's analysis, number of updates you can provide during the projects should be between {} and {}". format(int(avg_update), int(avg_update*1.1)+1)
				statement3 = "Based on our recommendation engine's analysis, duration of your project can be between {} and {}". format(int(avg_duration*0.9), int(avg_duration*1.1)+1)
				statement4 = "Based on our recommendation engine's analysis, number of levels for your projects can be between {} and {}". format(int(avg_level*0.9), int(avg_level*1.1)+1)

				# print(open_statement)
				st.write(open_statement)
				st.write(statement1)
				st.write(statement2)
				st.write(statement3)
				st.write(statement4)

			if counter == 1:
				open_statement = 'This is the first time someone is trying to do this creative project in the selected city. Previously, {} projects were posted based on your current selection of Category and Subcategory across USA. Out of which {} projects were successfull and {} projects were failed.'.format(total_projects, successful_project, failed_projects)
				statement1 = "Based on our recommendation engine's analysis, you can adjust between {} and {}". format(round(avg_goal*0.90,2), round(avg_goal*1.1,2))
				statement2 = "Based on our recommendation engine's analysis, number of updates you can provide during the projects should be between {} and {}". format(int(avg_update), int(avg_update*1.1)+1)
				statement3 = "Based on our recommendation engine's analysis, duration of your project can be between {} and {}". format(int(avg_duration*0.9), int(avg_duration*1.1)+1)
				statement4 = "Based on our recommendation engine's analysis, number of levels for your projects can be between {} and {}". format(int(avg_level*0.9), int(avg_level*1.1)+1)

				# print(open_statement)
				st.write(open_statement)
				st.write(statement1)
				st.write(statement2)
				st.write(statement3)
				st.write(statement4)

		else:
			st.markdown("<h2 style='text-align: center; color: orange;'>Warning</h2>", unsafe_allow_html=True)
			st.markdown("<p style='margin: 0px 0px 0px 0px;text-align: justify;'>No record found in previous data, please try again with different attributes</p>", unsafe_allow_html=True)

if st.sidebar.button('Use Cases'):
    js = "window.open('https://github.com/shaishav11/Kickstarter-Crowdfunding-Recommendation-Engine/blob/master/streamlit_app/Kickstarter_Web_Application_Use_Cases.pdf')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)













	