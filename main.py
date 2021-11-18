
import dc
import numpy as np
from datetime import datetime
import streamlit as st
import streamlit as st 
import pandas as pd
fno=['ABFRL','ACC','ABBOTINDIA','AARTIIND','ADANIENT','ADANIPORTS','ALKEM','AMARAJABAT','APLLTD','APOLLOTYRE','ASHOKLEY','ASIANPAINT','AUBANK','AUROPHARMA','AXISBANK','BAJAJ-AUTO','BAJAJFINSV','BAJFINANCE','BALKRISIND','BANDHANBNK','BEL','BERGEPAINT','BHARATFORG','BHARTIARTL','BHEL','BPCL','BRITANNIA','CADILAHC','CANBK','CHOLAFIN','CIPLA','COFORGE','CONCOR','APOLLOHOSP','COROMANDEL','CUMMINSIND','CANFINHOME','DABUR','ASTRAL','DEEPAKNTR','GODREJCP','BATAINDIA','HAL','DIVISLAB','DRREDDY','ESCORTS','EXIDEIND','FEDERALBNK','GAIL','GLENMARK','HDFCAMC','GODREJPROP','HINDUNILVR','GRANULES','GRASIM','HCLTECH','HDFC','ICICIGI','HINDALCO','HINDPETRO','ICICIBANK','ICICIPRULI','IGL','INDHOTEL','INDIGO','INDUSINDBK','IOC','BOSCHLTD','IEX','IRCTC','JINDALSTEL','JSWSTEEL','JUBLFOOD','KOTAKBANK','LALPATHLAB','LTI','LUPIN','M&M','IPCALAB','MARICO','METROPOLIS','MGL','COALINDIA','MINDTREE','MOTHERSUMI','MPHASIS','MRF','CROMPTON','LTTS','NATIONALUM','NAVINFLUOR','NESTLEIND','NMDC','NTPC','PETRONET','PFC','PIDILITIND','PNB','POWERGRID','PVR','RAMCOCEM','RBLBANK','RECLTD','RELIANCE','DELTACORP','SBILIFE','SBIN','SHREECEM','DIXON','SRF','NAUKRI','EICHERMOT','SRTRANSFIN','OFSS','POLYCAB','GMRINFRA','SUNPHARMA','GUJGASLTD','SUNTV','TATACHEM','TCS','TATACONSUM','TATAPOWER','TORNTPOWER','TATASTEEL','HDFCLIFE','TECHM','IBULHSGFIN','TITAN','TORNTPHARM','TVSMOTOR','ULTRACEMCO','UPL','VEDL','VOLTAS','ZEEL','INFY','JKCEMENT','L&TFH','AMBUJACEM','M&MFIN','MARUTI','MCDOWELL-N','NAM-INDIA','BIOCON','COLPAL','OBEROIRLTY','CUB','ONGC','PEL','PERSISTENT','PFIZER','DLF','PIIND','HEROMOTOCO','INDUSTOWER','TRENT','ITC','LT','MANAPPURAM','MFSL','MUTHOOTFIN','PAGEIND','SIEMENS','STAR','TATAMOTORS','BANKBARODA','INDIAMART','UBL','DALBHARAT','MCX','INDIACEM','SYNGENE','HAVELLS','HDFCBANK','LICHSGFIN','SAIL','WIPRO','IDFCFIRSTB','IDEA']
all_shares =[
    '20MICRONS',
    '21STCENMGM',
    '3MINDIA',
    '3PLAND',
    '5PAISA',
    '63MOONS',
    'A2ZINFRA',
    'AAKASH',
    'AAREYDRUGS',
    'AARON',
    'AARTIDRUGS',
    'AARTIIND',
    'AARTISURF',
    'AARVEEDEN',
    'AARVI',
    'AAVAS',
    'ABB',
    'ABBOTINDIA',
    'ABCAPITAL',
    'ABFRL',
    'ABMINTLLTD',
    'ACC',
    'ACCELYA',
    'ACCURACY',
    'ACE',
    'ACRYSIL',
    'ADANIENT',
    'ADANIGREEN',
    'ADANIPORTS',
    'ADANIPOWER',
    'ADANITRANS',
    'ADFFOODS',
    'ADL',
    'ADORWELD',
    'ADROITINFO',
    'ADSL',
    'ADVANIHOTR',
    'ADVENZYMES',
    'AEGISCHEM',
    'AFFLE',
    'AGARIND',
    'AGCNET',
    'AGRITECH',
    'AGROPHOS',
    'AHLADA',
    'AHLEAST',
    'AHLUCONT',
    'AHLWEST',
    'AIAENG',
    'AIRAN',
    'AJANTPHARM',
    'AJMERA',
    'AJOONI',
    'AJRINFRA',
    'AKASH',
    'AKG',
    'AKSHARCHEM',
    'AKSHOPTFBR',
    'AKZOINDIA',
    'ALANKIT',
    'ALBERTDAVD',
    'ALEMBICLTD',
    'ALICON',
    'ALKALI',
    'ALKEM',
    'ALKYLAMINE',
    'ALLCARGO',
    'ALLSEC',
    'ALMONDZ',
    'ALOKINDS',
    'ALPA',
    'ALPHAGEO',
    'ALPSINDUS',
    'AMARAJABAT',
    'AMBER',
    'AMBICAAGAR',
    'AMBIKCO',
    'AMBUJACEM',
    'AMDIND',
    'AMIORG',
    'AMJLAND',
    'AMRUTANJAN',
    'ANANTRAJ',
    'ANDHRACEMT',
    'ANDHRAPAP',
    'ANDHRSUGAR',
    'ANDREWYU',
    'ANGELBRKG',
    'ANIKINDS',
    'ANKITMETAL',
    'ANMOL',
    'ANSALAPI',
    'ANSALHSG',
    'ANUP',
    'ANURAS',
    'APARINDS',
    'APCL',
    'APCOTEXIND',
    'APEX',
    'APLAPOLLO',
    'APLLTD',
    'APOLLO',
    'APOLLOHOSP',
    'APOLLOPIPE',
    'APOLLOTYRE',
    'APOLSINHOT',
    'APTECHT',
    'APTUS',
    'ARCHIDPLY',
    'ARCHIES',
    'ARENTERP',
    'ARIES',
    'ARIHANT',
    'ARIHANTCAP',
    'ARIHANTSUP',
    'ARMANFIN',
    'AROGRANITE',
    'ARROWGREEN',
    'ARSHIYA',
    'ARSSINFRA',
    'ARTEMISMED',
    'ARVEE',
    'ARVIND',
    'ARVINDFASN',
    'ARVSMART',
    'ASAHIINDIA',
    'ASAHISONG',
    'ASAL',
    'ASALCBR',
    'ASHAPURMIN',
    'ASHIANA',
    'ASHIMASYN',
    'ASHOKA',
    'ASHOKLEY',
    'ASIAN-RE',
    'ASIANHOTNR',
    'ASIANPAINT',
    'ASIANTILES',
    'ASPINWALL',
    'ASTEC',
    'ASTERDM',
    'ASTRAL',
    'ASTRAMICRO',
    'ASTRAZEN',
    'ASTRON',
    'ATFL',
    'ATGL',
    'ATLANTA',
    'ATUL',
    'ATULAUTO',
    'AUBANK',
    'AURIONPRO',
    'AUROPHARMA',
    'AUSOMENT',
    'AUTOAXLES',
    'AUTOIND',
    'AVADHSUGAR',
    'AVANTIFEED',
    'AVTNPL',
    'AWHCL',
    'AXISBANK',
    'AXISCADES',
    'AYMSYNTEX',
    'BAFNAPH',
    'BAGFILMS',
    'BAJAJ-AUTO',
    'BAJAJCON',
    'BAJAJELEC',
    'BAJAJFINSV',
    'BAJAJHIND',
    'BAJAJHLDNG',
    'BAJFINANCE',
    'BALAJITELE',
    'BALAMINES',
    'BALAXI',
    'BALKRISIND',
    'BALLARPUR',
    'BALMLAWRIE',
    'BALPHARMA',
    'BALRAMCHIN',
    'BANARBEADS',
    'BANARISUG',
    'BANCOINDIA',
    'BANDHANBNK',
    'BANG',
    'BANKA',
    'BANKBARODA',
    'BANKINDIA',
    'BANSWRAS',
    'BARBEQUE',
    'BARTRONICS',
    'BASF',
    'BASML',
    'BASML-RE',
    'BATAINDIA',
    'BAYERCROP',
    'BBL',
    'BBTC',
    'BCG',
    'BCLIND',
    'BCP',
    'BDL',
    'BEARDSELL',
    'BECTORFOOD',
    'BEDMUTHA',
    'BEL',
    'BEML',
    'BEPL',
    'BERGEPAINT',
    'BESTAGRO',
    'BFINVEST',
    'BFUTILITIE',
    'BGRENERGY',
    'BHAGERIA',
    'BHAGYANGR',
    'BHAGYAPROP',
    'BHANDARI',
    'BHARATFORG',
    'BHARATGEAR',
    'BHARATRAS',
    'BHARATWIRE',
    'BHARTIARTL',
    'BHEL',
    'BIGBLOC',
    'BIL',
    'BINDALAGRO',
    'BIOCON',
    'BIOFILCHEM',
    'BIRLACABLE',
    'BIRLACORPN',
    'BIRLAMONEY',
    'BIRLATYRE',
    'BKMINDST',
    'BLBLIMITED',
    'BLISSGVS',
    'BLKASHYAP',
    'BLS',
    'BLUEDART',
    'BLUESTARCO',
    'BODALCHEM',
    'BOMDYEING',
    'BOROLTD',
    'BORORENEW',
    'BOSCHLTD',
    'BPCL',
    'BPL',
    'BRFL',
    'BRIGADE',
    'BRITANNIA',
    'BRNL',
    'BROOKS',
    'BSE',
    'BSHSL',
    'BSL',
    'BSOFT',
    'BURGERKING',
    'BURNPUR',
    'BUTTERFLY',
    'BVCL',
    'BYKE',
    'CADILAHC',
    'CALSOFT',
    'CAMLINFINE',
    'CAMS',
    'CANBK',
    'CANDC',
    'CANFINHOME',
    'CANTABIL',
    'CAPACITE',
    'CAPLIPOINT',
    'CAPTRUST',
    'CARBORUNIV',
    'CAREERP',
    'CARERATING',
    'CARTRADE',
    'CASTROLIND',
    'CCHHL',
    'CCL',
    'CDSL',
    'CEATLTD',
    'CEBBCO',
    'CELEBRITY',
    'CENTENKA',
    'CENTEXT',
    'CENTRALBK',
    'CENTRUM',
    'CENTUM',
    'CENTURYPLY',
    'CENTURYTEX',
    'CERA',
    'CEREBRAINT',
    'CESC',
    'CGCL',
    'CGPOWER',
    'CHALET',
    'CHAMBLFERT',
    'CHEMBOND',
    'CHEMCON',
    'CHEMFAB',
    'CHEMPLASTS',
    'CHENNPETRO',
    'CHOLAFIN',
    'CHOLAHLDNG',
    'CIGNITITEC',
    'CINELINE',
    'CINEVISTA',
    'CIPLA',
    'CLEAN',
    'CLEDUCATE',
    'CLNINDIA',
    'CLSEL',
    'CMICABLES',
    'COALINDIA',
    'COCHINSHIP',
    'COFFEEDAY',
    'COFORGE',
    'COLPAL',
    'COMPINFO',
    'COMPUSOFT',
    'CONCOR',
    'CONFIPET',
    'CONSOFINVT',
    'CONTROLPR',
    'CORALFINAC',
    'CORDSCABLE',
    'COROMANDEL',
    'COSMOFILMS',
    'COUNCODOS',
    'COX&KINGS',
    'CRAFTSMAN',
    'CREATIVE',
    'CREATIVEYE',
    'CREDITACC',
    'CREST',
    'CRISIL',
    'CROMPTON',
    'CSBBANK',
    'CTE',
    'CUB',
    'CUBEXTUB',
    'CUMMINSIND',
    'CUPID',
    'CYBERMEDIA',
    'CYBERTECH',
    'CYIENT',
    'DAAWAT',
    'DABUR',
    'DALBHARAT',
    'DALMIASUG',
    'DAMODARIND',
    'DANGEE',
    'DATAMATICS',
    'DBCORP',
    'DBL',
    'DBREALTY',
    'DBSTOCKBRO',
    'DCAL',
    'DCBBANK',
    'DCM',
    'DCMFINSERV',
    'DCMNVL',
    'DCMSHRIRAM',
    'DCW',
    'DECCANCE',
    'DEEPAKFERT',
    'DEEPAKNTR',
    'DEEPENR',
    'DEEPINDS',
    'DELPHIFX',
    'DELTACORP',
    'DELTAMAGNT',
    'DEN',
    'DENORA',
    'DEVYANI',
    'DFMFOODS',
    'DGCONTENT',
    'DHAMPURSUG',
    'DHANBANK',
    'DHANI',
    'DHANUKA',
    'DHARSUGAR',
    'DHUNINV',
    'DIAMONDYD',
    'DIAPOWER',
    'DICIND',
    'DIGISPICE',
    'DISHTV',
    'DIVISLAB',
    'DIXON',
    'DLF',
    'DLINKINDIA',
    'DMART',
    'DNAMEDIA',
    'DODLA',
    'DOLAT',
    'DOLLAR',
    'DONEAR',
    'DPABHUSHAN',
    'DPSCLTD',
    'DPWIRES',
    'DRCSYSTEMS',
    'DREDGECORP',
    'DRREDDY',
    'DSSL',
    'DTIL',
    'DUCON',
    'DVL',
    'DWARKESH',
    'DYNAMATECH',
    'DYNPRO',
    'EASEMYTRIP',
    'EASTSILK',
    'EASUNREYRL',
    'ECLERX',
    'EDELWEISS',
    'EDUCOMP',
    'EICHERMOT',
    'EIDPARRY',
    'EIHAHOTELS',
    'EIHOTEL',
    'EIMCOELECO',
    'EKC',
    'ELECON',
    'ELECTCAST',
    'ELECTHERM',
    'ELGIEQUIP',
    'ELGIRUBCO',
    'EMAMILTD',
    'EMAMIPAP',
    'EMAMIREAL',
    'EMCO',
    'EMKAY',
    'EMMBI',
    'ENDURANCE',
    'ENERGYDEV',
    'ENGINERSIN',
    'ENIL',
    'EPL',
    'EQUITAS',
    'EQUITASBNK',
    'ERIS',
    'EROSMEDIA',
    'ESABINDIA',
    'ESCORTS',
    'ESSARSHPNG',
    'ESTER',
    'EVEREADY',
    'EVERESTIND',
    'EXCEL',
    'EXCELINDUS',
    'EXIDEIND',
    'EXPLEOSOL',
    'EXXARO',
    'FACT',
    'FAIRCHEMOR',
    'FCL',
    'FCONSUMER',
    'FCSSOFT',
    'FDC',
    'FEDERALBNK',
    'FEL',
    'FELDVR',
    'FIEMIND',
    'FILATEX',
    'FINCABLES',
    'FINEORG',
    'FINPIPE',
    'FLEXITUFF',
    'FLFL',
    'FLUOROCHEM',
    'FMGOETZE',
    'FMNL',
    'FORCEMOT',
    'FORTIS',
    'FOSECOIND',
    'FRETAIL',
    'FSC',
    'FSL',
    'GABRIEL',
    'GAEL',
    'GAIL',
    'GAL',
    'GALAXYSURF',
    'GALLANTT',
    'GALLISPAT',
    'GANDHITUBE',
    'GANECOS',
    'GANESHBE',
    'GANESHHOUC',
    'GANGAFORGE',
    'GANGESSECU',
    'GARFIBRES',
    'GATI',
    'GAYAPROJ',
    'GDL',
    'GEECEE',
    'GEEKAYWIRE',
    'GENCON',
    'GENESYS',
    'GENUSPAPER',
    'GENUSPOWER',
    'GEOJITFSL',
    'GEPIL',
    'GESHIP',
    'GET&D',
    'GFLLIMITED',
    'GFSTEELS',
    'GHCL',
    'GICHSGFIN',
    'GICRE',
    'GILLANDERS',
    'GILLETTE',
    'GINNIFILA',
    'GIPCL',
    'GISOLUTION',
    'GKWLIMITED',
    'GLAND',
    'GLAXO',
    'GLENMARK',
    'GLFL',
    'GLOBAL',
    'GLOBALVECT',
    'GLOBE',
    'GLOBUSSPR',
    'GLS',
    'GMBREW',
    'GMDCLTD',
    'GMMPFAUDLR',
    'GMRINFRA',
    'GNA',
    'GNFC',
    'GOACARBON',
    'GOCLCORP',
    'GODFRYPHLP',
    'GODHA',
    'GODREJAGRO',
    'GODREJCP',
    'GODREJIND',
    'GODREJPROP',
    'GOENKA',
    'GOKEX',
    'GOKUL',
    'GOKULAGRO',
    'GOLDENTOBC',
    'GOLDIAM',
    'GOLDTECH',
    'GOODLUCK',
    'GOODYEAR',
    'GPIL',
    'GPPL',
    'GPTINFRA',
    'GRANULES',
    'GRAPHITE',
    'GRASIM',
    'GRAUWEIL',
    'GRAVITA',
    'GREAVESCOT',
    'GREENLAM',
    'GREENPANEL',
    'GREENPLY',
    'GREENPOWER',
    'GRINDWELL',
    'GRINFRA',
    'GROBTEA',
    'GRPLTD',
    'GRSE',
    'GSCLCEMENT',
    'GSFC',
    'GSPL',
    'GSS',
    'GTL',
    'GTLINFRA',
    'GTNTEX',
    'GTPL',
    'GUFICBIO',
    'GUJALKALI',
    'GUJAPOLLO',
    'GUJGASLTD',
    'GUJRAFFIA',
    'GULFOILLUB',
    'GULFPETRO',
    'GULPOLY',
    'HAL',
    'HAPPSTMNDS',
    'HARRMALAYA',
    'HATHWAY',
    'HATSUN',
    'HAVELLS',
    'HAVISHA',
    'HBLPOWER',
    'HBSL',
    'HCC',
    'HCG',
    'HCL-INSYS',
    'HCLTECH',
    'HDFC',
    'HDFCAMC',
    'HDFCBANK',
    'HDFCLIFE',
    'HDIL',
    'HEG',
    'HEIDELBERG',
    'HEMIPROP',
    'HERANBA',
    'HERCULES',
    'HERITGFOOD',
    'HEROMOTOCO',
    'HESTERBIO',
    'HEXATRADEX',
    'HFCL',
    'HGINFRA',
    'HGS',
    'HIKAL',
    'HIL',
    'HILTON',
    'HIMATSEIDE',
    'HINDALCO',
    'HINDCOMPOS',
    'HINDCON',
    'HINDCOPPER',
    'HINDMOTORS',
    'HINDNATGLS',
    'HINDOILEXP',
    'HINDPETRO',
    'HINDUNILVR',
    'HINDZINC',
    'HIRECT',
    'HISARMETAL',
    'HITECH',
    'HITECHCORP',
    'HITECHGEAR',
    'HLEGLAS',
    'HLVLTD',
    'HMT',
    'HMVL',
    'HNDFDS',
    'HOMEFIRST',
    'HONAUT',
    'HONDAPOWER',
    'HOVS',
    'HPL',
    'HSCL',
    'HSIL',
    'HTMEDIA',
    'HUBTOWN',
    'HUDCO',
    'HUHTAMAKI',
    'IBREALEST',
    'IBULHSGFIN',
    'ICDSLTD',
    'ICEMAKE',
    'ICICIBANK',
    'ICICIGI',
    'ICICIPRULI',
    'ICIL',
    'ICRA',
    'IDBI',
    'IDEA',
    'IDFC',
    'IDFCFIRSTB',
    'IEX',
    'IFBAGRO',
    'IFBIND',
    'IFCI',
    'IFGLEXPOR',
    'IGARASHI',
    'IGL',
    'IGPL',
    'IIFL',
    'IIFLSEC',
    'IIFLWAM',
    'IITL',
    'IL&FSENGG',
    'IL&FSTRANS',
    'IMAGICAA',
    'IMFA',
    'IMPAL',
    'INCREDIBLE',
    'INDBANK',
    'INDHOTEL',
    'INDIACEM',
    'INDIAGLYCO',
    'INDIAMART',
    'INDIANB',
    'INDIANCARD',
    'INDIANHUME',
    'INDIGO',
    'INDIGOPNTS',
    'INDLMETER',
    'INDNIPPON',
    'INDOCO',
    'INDORAMA',
    'INDOSOLAR',
    'INDOSTAR',
    'INDOTECH',
    'INDOTHAI',
    'INDOWIND',
    'INDRAMEDCO',
    'INDSWFTLAB',
    'INDSWFTLTD',
    'INDTERRAIN',
    'INDUSINDBK',
    'INDUSTOWER',
    'INEOSSTYRO',
    'INFIBEAM',
    'INFOBEAN',
    'INFY',
    'INGERRAND',
    'INOXLEISUR',
    'INOXWIND',
    'INSECTICID',
    'INSPIRISYS',
    'INTELLECT',
    'INTENTECH',
    'INTLCONV',
    'INVENTURE',
    'IOB',
    'IOC',
    'IOLCP',
    'IPCALAB',
    'IPL',
    'IRB',
    'IRCON',
    'IRCTC',
    'IRFC',
    'IRISDOREME',
    'ISEC',
    'ISFT',
    'ISGEC',
    'ISMTLTD',
    'ITC',
    'ITDC',
    'ITDCEM',
    'ITI',
    'IVC',
    'IVP',
    'IWEL',
    'IZMO',
    'J&KBANK',
    'JAGRAN',
    'JAGSNPHARM',
    'JAIBALAJI',
    'JAICORPLTD',
    'JAINSTUDIO',
    'JAIPURKURT',
    'JAMNAAUTO',
    'JASH',
    'JAYAGROGN',
    'JAYBARMARU',
    'JAYNECOIND',
    'JAYSREETEA',
    'JBCHEPHARM',
    'JBFIND',
    'JBMA',
    'JCHAC',
    'JETAIRWAYS',
    'JHS',
    'JINDALPHOT',
    'JINDALPOLY',
    'JINDALSAW',
    'JINDALSTEL',
    'JINDRILL',
    'JINDWORLD',
    'JISLDVREQS',
    'JISLJALEQS',
    'JITFINFRA',
    'JKCEMENT',
    'JKIL',
    'JKLAKSHMI',
    'JKPAPER',
    'JKTYRE',
    'JMA',
    'JMCPROJECT',
    'JMFINANCIL',
    'JMTAUTOLTD',
    'JOCIL',
    'JPASSOCIAT',
    'JPINFRATEC',
    'JPOLYINVST',
    'JPPOWER',
    'JSL',
    'JSLHISAR',
    'JSWENERGY',
    'JSWHL',
    'JSWISPL',
    'JSWSTEEL',
    'JTEKTINDIA',
    'JUBLFOOD',
    'JUBLINDS',
    'JUBLINGREA',
    'JUBLPHARMA',
    'JUMPNET',
    'JUSTDIAL',
    'JYOTHYLAB',
    'JYOTISTRUC',
    'KABRAEXTRU',
    'KAJARIACER',
    'KAKATCEM',
    'KALPATPOWR',
    'KALYANI',
    'KALYANIFRG',
    'KALYANKJIL',
    'KAMATHOTEL',
    'KAMDHENU',
    'KANANIIND',
    'KANORICHEM',
    'KANPRPLA',
    'KANSAINER',
    'KAPSTON',
    'KARDA',
    'KARMAENG',
    'KARURVYSYA',
    'KAUSHALYA',
    'KAVVERITEL',
    'KAYA',
    'KCP',
    'KCPSUGIND',
    'KDDL',
    'KEC',
    'KECL',
    'KEERTI',
    'KEI',
    'KELLTONTEC',
    'KENNAMET',
    'KERNEX',
    'KESORAMIND',
    'KEYFINSERV',
    'KHADIM',
    'KHAICHEM',
    'KHAITANLTD',
    'KHANDSE',
    'KICL',
    'KIL-RE',
    'KILITCH',
    'KIMS',
    'KINGFA',
    'KIOCL',
    'KIRIINDUS',
    'KIRLFER',
    'KIRLOSBROS',
    'KIRLOSENG',
    'KIRLOSIND',
    'KITEX',
    'KKCL',
    'KMSUGAR',
    'KNRCON',
    'KOKUYOCMLN',
    'KOLTEPATIL',
    'KOPRAN',
    'KOTAKBANK',
    'KOTARISUG',
    'KOTHARIPET',
    'KOTHARIPRO',
    'KOVAI',
    'KPIGLOBAL',
    'KPITTECH',
    'KPRMILL',
    'KRBL',
    'KREBSBIO',
    'KRIDHANINF',
    'KRISHANA',
    'KRSNAA',
    'KSB',
    'KSCL',
    'KSL',
    'KTKBANK',
    'KUANTUM',
    'L&TFH',
    'LAKPRE',
    'LALPATHLAB',
    'LAMBODHARA',
    'LAOPALA',
    'LASA',
    'LAURUSLABS',
    'LAXMIMACH',
    'LCCINFOTEC',
    'LEMONTREE',
    'LFIC',
    'LGBBROSLTD',
    'LGBFORGE',
    'LIBAS',
    'LIBERTSHOE',
    'LICHSGFIN',
    'LIKHITHA',
    'LINCOLN',
    'LINCPEN',
    'LINDEINDIA',
    'LODHA',
    'LOKESHMACH',
    'LOTUSEYE',
    'LOVABLE',
    'LPDC',
    'LSIL',
    'LT',
    'LTI',
    'LTTS',
    'LUMAXIND',
    'LUMAXTECH',
    'LUPIN',
    'LUXIND',
    'LXCHEM',
    'LYKALABS',
    'LYPSAGEMS',
    'M&M',
    'M&MFIN',
    'MAANALU',
    'MACPOWER',
    'MADHAV',
    'MADHUCON',
    'MADRASFERT',
    'MAGADSUGAR',
    'MAGNUM',
    'MAHABANK',
    'MAHAPEXLTD',
    'MAHASTEEL',
    'MAHEPC',
    'MAHESHWARI',
    'MAHINDCIE',
    'MAHLIFE',
    'MAHLOG',
    'MAHSCOOTER',
    'MAHSEAMLES',
    'MAITHANALL',
    'MAJESCO',
    'MALUPAPER',
    'MANAKALUCO',
    'MANAKCOAT',
    'MANAKSIA',
    'MANAKSTEEL',
    'MANALIPETC',
    'MANAPPURAM',
    'MANGALAM',
    'MANGCHEFER',
    'MANGLMCEM',
    'MANGTIMBER',
    'MANINDS',
    'MANINFRA',
    'MANUGRAPH',
    'MARALOVER',
    'MARATHON',
    'MARICO',
    'MARINE',
    'MARKSANS',
    'MARUTI',
    'MASFIN',
    'MASKINVEST',
    'MASTEK',
    'MATRIMONY',
    'MAWANASUG',
    'MAXHEALTH',
    'MAXIND',
    'MAXVIL',
    'MAYURUNIQ',
    'MAZDA',
    'MAZDOCK',
    'MBAPL',
    'MBECL',
    'MBLINFRA',
    'MCDHOLDING',
    'MCDOWELL-N',
    'MCL',
    'MCLEODRUSS',
    'MCX',
    'MEGASOFT',
    'MELSTAR',
    'MENONBE',
    'MEP',
    'MERCATOR',
    'METALFORGE',
    'METROPOLIS',
    'MFL',
    'MFSL',
    'MGEL',
    'MGL',
    'MHRIL',
    'MIDHANI',
    'MINDACORP',
    'MINDAIND',
    'MINDTECK',
    'MINDTREE',
    'MIRCELECTR',
    'MIRZAINT',
    'MITTAL',
    'MMFL',
    'MMP',
    'MMTC',
    'MODIRUBBER',
    'MODISNME',
    'MOHITIND',
    'MOHOTAIND',
    'MOIL',
    'MOKSH',
    'MOL',
    'MOLDTECH',
    'MOLDTKPAC',
    'MONTECARLO',
    'MORARJEE',
    'MOREPENLAB',
    'MOTHERSUMI',
    'MOTILALOFS',
    'MOTOGENFIN',
    'MPHASIS',
    'MPSLTD',
    'MRF',
    'MRO-TEK',
    'MRPL',
    'MSPL',
    'MSTCLTD',
    'MTARTECH',
    'MTEDUCARE',
    'MTNL',
    'MUKANDLTD',
    'MUKTAARTS',
    'MUNJALAU',
    'MUNJALSHOW',
    'MURUDCERA',
    'MUTHOOTCAP',
    'MUTHOOTFIN',
    'NACLIND',
    'NAGAFERT',
    'NAGREEKCAP',
    'NAGREEKEXP',
    'NAHARCAP',
    'NAHARINDUS',
    'NAHARPOLY',
    'NAHARSPING',
    'NAM-INDIA',
    'NATCOPHARM',
    'NATHBIOGEN',
    'NATIONALUM',
    'NATNLSTEEL',
    'NAUKRI',
    'NAVINFLUOR',
    'NAVKARCORP',
    'NAVNETEDUL',
    'NAZARA',
    'NBCC',
    'NBIFIN',
    'NBVENTURES',
    'NCC',
    'NCLIND',
    'NDGL',
    'NDL',
    'NDRAUTO',
    'NDTV',
    'NECCLTD',
    'NECLIFE',
    'NELCAST',
    'NELCO',
    'NEOGEN',
    'NESCO',
    'NESTLEIND',
    'NETWORK18',
    'NEULANDLAB',
    'NEWGEN',
    'NEXTMEDIA',
    'NFL',
    'NGIL',
    'NH',
    'NHPC',
    'NIACL',
    'NIBL',
    'NIITLTD',
    'NILAINFRA',
    'NILASPACES',
    'NILKAMAL',
    'NIPPOBATRY',
    'NIRAJ',
    'NIRAJISPAT',
    'NITCO',
    'NITINFIRE',
    'NITINSPIN',
    'NITIRAJ',
    'NKIND',
    'NLCINDIA',
    'NMDC',
    'NOCIL',
    'NOIDATOLL',
    'NORBTEAEXP',
    'NOVARTIND',
    'NRAIL',
    'NRBBEARING',
    'NSIL',
    'NTL',
    'NTPC',
    'NUCLEUS',
    'NURECA',
    'NUVOCO',
    'NXTDIGITAL',
    'OAL',
    'OBEROIRLTY',
    'OCCL',
    'OFSS',
    'OIL',
    'OILCOUNTUB',
    'OLECTRA',
    'OMAXAUTO',
    'OMAXE',
    'OMINFRAL',
    'OMKARCHEM',
    'ONELIFECAP',
    'ONEPOINT',
    'ONGC',
    'ONMOBILE',
    'ONWARDTEC',
    'OPTIEMUS',
    'OPTOCIRCUI',
    'ORBTEXP',
    'ORCHPHARMA',
    'ORICONENT',
    'ORIENTABRA',
    'ORIENTALTL',
    'ORIENTBELL',
    'ORIENTCEM',
    'ORIENTELEC',
    'ORIENTHOT',
    'ORIENTLTD',
    'ORIENTPPR',
    'ORISSAMINE',
    'ORTEL',
    'ORTINLAB',
    'OSWALAGRO',
    'PAEL',
    'PAGEIND',
    'PAISALO',
    'PALASHSECU',
    'PALREDTEC',
    'PANACEABIO',
    'PANACHE',
    'PANAMAPET',
    'PAR',
    'PARACABLES',
    'PARAGMILK',
    'PARSVNATH',
    'PATELENG',
    'PATINTLOG',
    'PATSPINLTD',
    'PBAINFRA',
    'PCJEWELLER',
    'PDMJEPAPER',
    'PDSMFL',
    'PEARLPOLY',
    'PEL',
    'PENIND',
    'PENINLAND',
    'PERSISTENT',
    'PETRONET',
    'PFC',
    'PFIZER',
    'PFOCUS',
    'PFS',
    'PGEL',
    'PGHH',
    'PGHL',
    'PGIL',
    'PHILIPCARB',
    'PHOENIXLTD',
    'PIDILITIND',
    'PIIND',
    'PILANIINVS',
    'PILITA',
    'PIONDIST',
    'PIONEEREMB',
    'PITTIENG',
    'PKTEA',
    'PLASTIBLEN',
    'PNB',
    'PNBGILTS',
    'PNBHOUSING',
    'PNC',
    'PNCINFRA',
    'PODDARHOUS',
    'PODDARMENT',
    'POKARNA',
    'POLYCAB',
    'POLYMED',
    'POLYPLEX',
    'PONNIERODE',
    'POONAWALLA',
    'POWERGRID',
    'POWERINDIA',
    'POWERMECH',
    'PPAP',
    'PPL',
    'PRAENG',
    'PRAJIND',
    'PRAKASH',
    'PRAKASHSTL',
    'PRAXIS',
    'PRAXIS-RE',
    'PRECAM',
    'PRECOT',
    'PRECWIRE',
    'PREMEXPLN',
    'PREMIER',
    'PREMIERPOL',
    'PRESSMN',
    'PRESTIGE',
    'PRICOLLTD',
    'PRIMESECU',
    'PRINCEPIPE',
    'PRITIKAUTO',
    'PRIVISCL',
    'PROINDIA',
    'PROZONINTU',
    'PRSMJOHNSN',
    'PSB',
    'PSPPROJECT',
    'PTC',
    'PTL',
    'PUNJABCHEM',
    'PUNJLLOYD',
    'PURVA',
    'PVP',
    'PVR',
    'QUESS',
    'QUICKHEAL',
    'RADAAN',
    'RADICO',
    'RADIOCITY',
    'RAILTEL',
    'RAIN',
    'RAJESHEXPO',
    'RAJMET',
    'RAJRATAN',
    'RAJRAYON',
    'RAJSREESUG',
    'RAJTV',
    'RALLIS',
    'RAMANEWS',
    'RAMASTEEL',
    'RAMCOCEM',
    'RAMCOIND',
    'RAMCOSYS',
    'RAMKY',
    'RANASUG',
    'RANEENGINE',
    'RANEHOLDIN',
    'RATNAMANI',
    'RAYMOND',
    'RBL',
    'RBLBANK',
    'RCF',
    'RCOM',
    'RECLTD',
    'REDINGTON',
    'REFEX',
    'RELAXO',
    'RELCAPITAL',
    'RELIANCE',
    'RELIGARE',
    'RELINFRA',
    'REMSONSIND',
    'RENUKA',
    'REPCOHOME',
    'REPL',
    'REPRO',
    'RESPONIND',
    'REVATHI',
    'RGL',
    'RHFL',
    'RHIM',
    'RICOAUTO',
    'RIIL',
    'RITES',
    'RKDL',
    'RKEC',
    'RKFORGE',
    'RMCL',
    'RML',
    'RNAVAL',
    'ROHITFERRO',
    'ROHLTD',
    'ROLEXRINGS',
    'ROLLT',
    'ROLTA',
    'ROML',
    'ROSSARI',
    'ROSSELLIND',
    'ROUTE',
    'RPGLIFE',
    'RPOWER',
    'RPP-RE',
    'RPPINFRA',
    'RPSGVENT',
    'RSSOFTWARE',
    'RSWM',
    'RSYSTEMS',
    'RTNINDIA',
    'RTNPOWER',
    'RUBYMILLS',
    'RUCHI',
    'RUCHINFRA',
    'RUCHIRA',
    'RUPA',
    'RUSHIL',
    'RVHL',
    'RVNL',
    'S&SPOWER',
    'SABEVENTS',
    'SABTN',
    'SADBHAV',
    'SADBHIN',
    'SAFARI',
    'SAGARDEEP',
    'SAGCEM',
    'SAIL',
    'SAKAR',
    'SAKHTISUG',
    'SAKSOFT',
    'SAKUMA',
    'SALASAR',
    'SALONA',
    'SALSTEEL',
    'SALZERELEC',
    'SAMBHAAV',
    'SANCO',
    'SANDESH',
    'SANDHAR',
    'SANGAMIND',
    'SANGHIIND',
    'SANGHVIMOV',
    'SANGINITA',
    'SANOFI',
    'SANSERA',
    'SANWARIA',
    'SARDAEN',
    'SAREGAMA',
    'SARLAPOLY',
    'SASKEN',
    'SASTASUNDR',
    'SATIA',
    'SATIN',
    'SBCL',
    'SBICARD',
    'SBILIFE',
    'SBIN',
    'SCAPDVR',
    'SCHAEFFLER',
    'SCHAND',
    'SCHNEIDER',
    'SCI',
    'SDBL',
    'SEAMECLTD',
    'SECURKLOUD',
    'SELAN',
    'SEPOWER',
    'SEQUENT',
    'SERVOTECH',
    'SESHAPAPER',
    'SETCO',
    'SETUINFRA',
    'SEYAIND',
    'SFL',
    'SGIL',
    'SGL',
    'SHAHALLOYS',
    'SHAKTIPUMP',
    'SHALBY',
    'SHALPAINTS',
    'SHANKARA',
    'SHANTI',
    'SHANTIGEAR',
    'SHARDACROP',
    'SHARDAMOTR',
    'SHAREINDIA',
    'SHEMAROO',
    'SHIL',
    'SHILPAMED',
    'SHIVAMAUTO',
    'SHIVAMILLS',
    'SHIVATEX',
    'SHK',
    'SHOPERSTOP',
    'SHRADHA',
    'SHREDIGCEM',
    'SHREECEM',
    'SHREEPUSHK',
    'SHREERAMA',
    'SHRENIK',
    'SHREYANIND',
    'SHREYAS',
    'SHRIPISTON',
    'SHRIRAMCIT',
    'SHRIRAMEPC',
    'SHYAMCENT',
    'SHYAMMETL',
    'SHYAMTEL',
    'SICAL',
    'SIEMENS',
    'SIGIND',
    'SIL',
    'SILGO',
    'SILINV',
    'SILLYMONKS',
    'SIMBHALS',
    'SIMPLEXINF',
    'SINTERCOM',
    'SINTEX',
    'SIRCA',
    'SIS',
    'SITINET',
    'SIYSIL',
    'SJVN',
    'SKFINDIA',
    'SKIL',
    'SKIPPER',
    'SKMEGGPROD',
    'SMARTLINK',
    'SMCGLOBAL',
    'SMLISUZU',
    'SMSLIFE',
    'SMSPHARMA',
    'SNOWMAN',
    'SOBHA',
    'SOLARA',
    'SOLARINDS',
    'SOMANYCERA',
    'SOMATEX',
    'SOMICONVEY',
    'SONACOMS',
    'SONATSOFTW',
    'SORILINFRA',
    'SOTL',
    'SOUTHBANK',
    'SOUTHWEST',
    'SPAL',
    'SPANDANA',
    'SPARC',
    'SPECIALITY',
    'SPENCERS',
    'SPENTEX',
    'SPIC',
    'SPICEJET',
    'SPLIL',
    'SPMLINFRA',
    'SPTL',
    'SREEL',
    'SREINFRA',
    'SRF',
    'SRHHYPOLTD',
    'SRIPIPES',
    'SRPL',
    'SRTRANSFIN',
    'SSWL',
    'STAR',
    'STARCEMENT',
    'STARPAPER',
    'STCINDIA',
    'STEELCITY',
    'STEELXIND',
    'STEL',
    'STERTOOLS',
    'STLTECH',
    'STOVEKRAFT',
    'STYLAMIND',
    'SUBCAPCITY',
    'SUBEXLTD',
    'SUBROS',
    'SUDARSCHEM',
    'SUMEETINDS',
    'SUMICHEM',
    'SUMIT',
    'SUMMITSEC',
    'SUNCLAYLTD',
    'SUNDARAM',
    'SUNDARMFIN',
    'SUNDARMHLD',
    'SUNDRMBRAK',
    'SUNDRMFAST',
    'SUNFLAG',
    'SUNPHARMA',
    'SUNTECK',
    'SUNTV',
    'SUPERHOUSE',
    'SUPERSPIN',
    'SUPPETRO',
    'SUPRAJIT',
    'SUPREMEENG',
    'SUPREMEIND',
    'SURANASOL',
    'SURANAT&P',
    'SURYALAXMI',
    'SURYAROSNI',
    'SURYODAY',
    'SUTLEJTEX',
    'SUULD',
    'SUVEN',
    'SUVENPHAR',
    'SUVIDHAA',
    'SUZLON',
    'SVPGLOB',
    'SWANENERGY',
    'SWARAJENG',
    'SWELECTES',
    'SWSOLAR',
    'SYMPHONY',
    'SYNGENE',
    'TAINWALCHM',
    'TAJGVK',
    'TAKE',
    'TALBROAUTO',
    'TANLA',
    'TANTIACONS',
    'TARAPUR',
    'TARC',
    'TARMAT',
    'TASTYBITE',
    'TATACHEM',
    'TATACOFFEE',
    'TATACOMM',
    'TATACONSUM',
    'TATAELXSI',
    'TATAINVEST',
    'TATAMETALI',
    'TATAMOTORS',
    'TATAMTRDVR',
    'TATAPOWER',
    'TATASTEEL',
    'TATASTLBSL',
    'TATASTLLP',
    'TATVA',
    'TBZ',
    'TCI',
    'TCIDEVELOP',
    'TCIEXP',
    'TCIFINANCE',
    'TCNSBRANDS',
    'TCPLPACK',
    'TCS',
    'TDPOWERSYS',
    'TEAMLEASE',
    'TECHIN',
    'TECHM',
    'TECHNOE',
    'TEJASNET',
    'TEMBO',
    'TERASOFT',
    'TEXINFRA',
    'TEXMOPIPES',
    'TEXRAIL',
    'TFCILTD',
    'TFL',
    'TGBHOTELS',
    'THANGAMAYL',
    'THEINVEST',
    'THEMISMED',
    'THERMAX',
    'THOMASCOOK',
    'THOMASCOTT',
    'THYROCARE',
    'TI',
    'TIDEWATER',
    'TIIL',
    'TIINDIA',
    'TIJARIA',
    'TIL',
    'TIMESGTY',
    'TIMETECHNO',
    'TIMKEN',
    'TINPLATE',
    'TIPSINDLTD',
    'TIRUMALCHM',
    'TIRUPATIFL',
    'TITAN',
    'TMRVL',
    'TNPETRO',
    'TNPL',
    'TNTELE',
    'TOKYOPLAST',
    'TORNTPHARM',
    'TORNTPOWER',
    'TOTAL',
    'TOUCHWOOD',
    'TPLPLASTEH',
    'TREEHOUSE',
    'TREJHARA',
    'TRENT',
    'TRF',
    'TRIDENT',
    'TRIGYN',
    'TRIL',
    'TRITURBINE',
    'TRIVENI',
    'TTKHLTCARE',
    'TTKPRESTIG',
    'TTL',
    'TTML',
    'TV18BRDCST',
    'TVSELECT',
    'TVSMOTOR',
    'TVSSRICHAK',
    'TVTODAY',
    'TVVISION',
    'TWL',
    'UBL',
    'UCALFUEL',
    'UCOBANK',
    'UFLEX',
    'UFO',
    'UGARSUGAR',
    'UGROCAP',
    'UJAAS',
    'UJJIVAN',
    'UJJIVANSFB',
    'ULTRACEMCO',
    'UMANGDAIRY',
    'UMESLTD',
    'UNICHEMLAB',
    'UNIDT',
    'UNIENTER',
    'UNIONBANK',
    'UNITECH',
    'UNITEDTEA',
    'UNIVASTU',
    'UNIVCABLES',
    'UNIVPHOTO',
    'UPL',
    'URJA',
    'USHAMART',
    'UTIAMC',
    'UTTAMSTL',
    'UTTAMSUGAR',
    'V2RETAIL',
    'VADILALIND',
    'VAIBHAVGBL',
    'VAISHALI',
    'VAKRANGEE',
    'VALIANTORG',
    'VARDHACRLC',
    'VARDMNPOLY',
    'VARROC',
    'VASCONEQ',
    'VASWANI',
    'VBL',
    'VEDL',
    'VENKEYS',
    'VENUSREM',
    'VERTOZ',
    'VESUVIUS',
    'VETO',
    'VGUARD',
    'VHL',
    'VICEROY',
    'VIDHIING',
    'VIJAYA',
    'VIJIFIN',
    'VIKASECO',
    'VIKASLIFE',
    'VIKASPROP',
    'VIKASWSP',
    'VIMTALABS',
    'VINATIORGA',
    'VINDHYATEL',
    'VINEETLAB',
    'VINYLINDIA',
    'VIPCLOTHNG',
    'VIPIND',
    'VIPULLTD',
    'VISAKAIND',
    'VISASTEEL',
    'VISHAL',
    'VISHNU',
    'VISHWARAJ',
    'VIVIDHA',
    'VIVIMEDLAB',
    'VLSFINANCE',
    'VMART',
    'VOLTAMP',
    'VOLTAS',
    'VRLLOG',
    'VSSL',
    'VSTIND',
    'VSTTILLERS',
    'VTL',
    'WABAG',
    'WABCOINDIA',
    'WALCHANNAG',
    'WANBURY',
    'WATERBASE',
    'WEALTH',
    'WEBELSOLAR',
    'WEIZMANIND',
    'WELCORP',
    'WELENT',
    'WELINV',
    'WELSPUNIND',
    'WENDT',
    'WESTLIFE',
    'WHEELS',
    'WHIRLPOOL',
    'WILLAMAGOR',
    'WINDLAS',
    'WINDMACHIN',
    'WIPL',
    'WIPRO',
    'WOCKPHARMA',
    'WONDERLA',
    'WORTH',
    'WSI',
    'WSTCSTPAPR',
    'XCHANGING',
    'XELPMOC',
    'XPROINDIA',
    'YAARII',
    'YESBANK',
    'YUKEN',
    'ZEEL',
    'ZEELEARN',
    'ZEEMEDIA',
    'ZENITHEXPO',
    'ZENSARTECH',
    'ZENTEC',
    'ZODIACLOTH',
    'ZOMATO',
    'ZOTA',
    'ZUARI',
    'ZUARIGLOB',
    'ZYDUSWELL',
    ]

period=st.sidebar.text_input("Enter donchian period like 20,30,50")
category=st.sidebar.selectbox('category',('fno', 'all'))
type1=st.sidebar.selectbox('Select type',('Daily Stocks',"Short time"))
price_limit = st.sidebar.text_input("Enter min price limit for filtering stocks")
if type1=='Daily Stocks':
    pr="3mo"
    interval="1d"
else:
    pr=st.sidebar.selectbox("time period",("5d","1mo",))
    interval=st.sidebar.selectbox("candlestick interval",("15m","30m","60m","90m","1h","2h"))
if category=="fno":
    shares=fno
else:
    shares=all_shares    
table=st.empty()
if st.sidebar.button("Submit"):
    ls=[]
#a_file = open("sample.csv", "w")
#writer = csv.writer(a_file)
#writer.writerow(["symbol","date"])
    for i in range(len(shares)):
        x=dc.get_alerts(shares[i],int(period),pr,interval)
        ls.append(x)
        ls=list(filter(lambda x: x, ls))
        df=pd.DataFrame(ls, columns =['symbol', 'last alert date'])
    #writer.writerow(x)
        table.dataframe(df)


#a_file.close()    
