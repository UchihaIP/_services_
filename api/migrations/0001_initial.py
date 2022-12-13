# Generated by Django 4.1.4 on 2022-12-13 17:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Client's phone number in the format [7XXXXXXXXXX] (X is a number from 0 to 9)", regex='^7\\d{10}$')], verbose_name="Client's phone number")),
                ('mobile_code', models.CharField(max_length=3, verbose_name='Mobile operator code')),
                ('tag', models.CharField(blank=True, max_length=20, verbose_name='Search filtering tag')),
                ('timezone', models.CharField(choices=[('Asia/Shanghai', 'Asia/Shanghai'), ('GMT', 'GMT'), ('Africa/Kigali', 'Africa/Kigali'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('America/Belem', 'America/Belem'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Chihuahua', 'America/Chihuahua'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Iqaluit', 'America/Iqaluit'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Goose_Bay', 'America/Goose_Bay'), ('America/Rosario', 'America/Rosario'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Africa/Banjul', 'Africa/Banjul'), ('Africa/Lusaka', 'Africa/Lusaka'), ('GB', 'GB'), ('NZ-CHAT', 'NZ-CHAT'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/Shiprock', 'America/Shiprock'), ('Etc/GMT+4', 'Etc/GMT+4'), ('America/Aruba', 'America/Aruba'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('GMT+0', 'GMT+0'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Pacific/Noumea', 'Pacific/Noumea'), ('EST', 'EST'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('America/Jamaica', 'America/Jamaica'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Asia/Beirut', 'Asia/Beirut'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('America/Tortola', 'America/Tortola'), ('America/Vancouver', 'America/Vancouver'), ('America/Swift_Current', 'America/Swift_Current'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Australia/Queensland', 'Australia/Queensland'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Atlantic/Azores', 'Atlantic/Azores'), ('UTC', 'UTC'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Toronto', 'America/Toronto'), ('Asia/Muscat', 'Asia/Muscat'), ('Etc/GMT+2', 'Etc/GMT+2'), ('America/Louisville', 'America/Louisville'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('ROC', 'ROC'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Recife', 'America/Recife'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Australia/Eucla', 'Australia/Eucla'), ('America/Juneau', 'America/Juneau'), ('Europe/Malta', 'Europe/Malta'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('CST6CDT', 'CST6CDT'), ('Europe/Vatican', 'Europe/Vatican'), ('Asia/Macau', 'Asia/Macau'), ('Africa/Algiers', 'Africa/Algiers'), ('Japan', 'Japan'), ('America/Thule', 'America/Thule'), ('Etc/UTC', 'Etc/UTC'), ('America/Antigua', 'America/Antigua'), ('Europe/Rome', 'Europe/Rome'), ('Asia/Manila', 'Asia/Manila'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Europe/Madrid', 'Europe/Madrid'), ('MST', 'MST'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Asia/Kuching', 'Asia/Kuching'), ('Europe/Oslo', 'Europe/Oslo'), ('America/Moncton', 'America/Moncton'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Zurich', 'Europe/Zurich'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Australia/Sydney', 'Australia/Sydney'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Catamarca', 'America/Catamarca'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Africa/Kampala', 'Africa/Kampala'), ('Pacific/Apia', 'Pacific/Apia'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Bogota', 'America/Bogota'), ('Kwajalein', 'Kwajalein'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Ensenada', 'America/Ensenada'), ('Europe/Lisbon', 'Europe/Lisbon'), ('America/Guatemala', 'America/Guatemala'), ('Africa/Tunis', 'Africa/Tunis'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/Rainy_River', 'America/Rainy_River'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Edmonton', 'America/Edmonton'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Miquelon', 'America/Miquelon'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Africa/Mbabane', 'Africa/Mbabane'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('EET', 'EET'), ('NZ', 'NZ'), ('Australia/Canberra', 'Australia/Canberra'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Malabo', 'Africa/Malabo'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Martinique', 'America/Martinique'), ('Africa/Luanda', 'Africa/Luanda'), ('America/Nassau', 'America/Nassau'), ('Pacific/Midway', 'Pacific/Midway'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Africa/Freetown', 'Africa/Freetown'), ('Israel', 'Israel'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Detroit', 'America/Detroit'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Cuba', 'Cuba'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Europe/Minsk', 'Europe/Minsk'), ('Africa/Conakry', 'Africa/Conakry'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Asia/Aden', 'Asia/Aden'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Europe/Brussels', 'Europe/Brussels'), ('GMT0', 'GMT0'), ('Etc/GMT-8', 'Etc/GMT-8'), ('US/Hawaii', 'US/Hawaii'), ('Asia/Hebron', 'Asia/Hebron'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Factory', 'Factory'), ('UCT', 'UCT'), ('Australia/West', 'Australia/West'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Indianapolis', 'America/Indianapolis'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('America/Winnipeg', 'America/Winnipeg'), ('Etc/GMT+6', 'Etc/GMT+6'), ('ROK', 'ROK'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Mexico_City', 'America/Mexico_City'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/St_Johns', 'America/St_Johns'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Asia/Almaty', 'Asia/Almaty'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('US/Mountain', 'US/Mountain'), ('Europe/Prague', 'Europe/Prague'), ('Asia/Qatar', 'Asia/Qatar'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Europe/Dublin', 'Europe/Dublin'), ('Australia/Tasmania', 'Australia/Tasmania'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Belize', 'America/Belize'), ('Mexico/General', 'Mexico/General'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('America/Curacao', 'America/Curacao'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('America/Noronha', 'America/Noronha'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Etc/Universal', 'Etc/Universal'), ('America/Fortaleza', 'America/Fortaleza'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Canada/Central', 'Canada/Central'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Europe/Samara', 'Europe/Samara'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Asia/Dili', 'Asia/Dili'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Saigon', 'Asia/Saigon'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('America/Havana', 'America/Havana'), ('Asia/Oral', 'Asia/Oral'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Inuvik', 'America/Inuvik'), ('Chile/Continental', 'Chile/Continental'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('MST7MDT', 'MST7MDT'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Europe/Budapest', 'Europe/Budapest'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Guadeloupe', 'America/Guadeloupe'), ('America/Montreal', 'America/Montreal'), ('US/Aleutian', 'US/Aleutian'), ('Indian/Chagos', 'Indian/Chagos'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Africa/Djibouti', 'Africa/Djibouti'), ('America/New_York', 'America/New_York'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Paramaribo', 'America/Paramaribo'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Chicago', 'America/Chicago'), ('PRC', 'PRC'), ('America/Ojinaga', 'America/Ojinaga'), ('America/El_Salvador', 'America/El_Salvador'), ('America/Creston', 'America/Creston'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Pacific/Gambier', 'Pacific/Gambier'), ('America/Panama', 'America/Panama'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Europe/Busingen', 'Europe/Busingen'), ('America/Sitka', 'America/Sitka'), ('Asia/Riyadh', 'Asia/Riyadh'), ('America/Cancun', 'America/Cancun'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Gaza', 'Asia/Gaza'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Dominica', 'America/Dominica'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Riga', 'Europe/Riga'), ('America/Yakutat', 'America/Yakutat'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Cayenne', 'America/Cayenne'), ('Pacific/Yap', 'Pacific/Yap'), ('Eire', 'Eire'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Antarctica/Casey', 'Antarctica/Casey'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Brunei', 'Asia/Brunei'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Maputo', 'Africa/Maputo'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Santiago', 'America/Santiago'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Nome', 'America/Nome'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Cuiaba', 'America/Cuiaba'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('WET', 'WET'), ('W-SU', 'W-SU'), ('America/Merida', 'America/Merida'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Asia/Magadan', 'Asia/Magadan'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Matamoros', 'America/Matamoros'), ('America/Halifax', 'America/Halifax'), ('Pacific/Easter', 'Pacific/Easter'), ('US/Michigan', 'US/Michigan'), ('America/Grenada', 'America/Grenada'), ('Europe/Berlin', 'Europe/Berlin'), ('America/Kralendijk', 'America/Kralendijk'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Asia/Seoul', 'Asia/Seoul'), ('Africa/Cairo', 'Africa/Cairo'), ('America/Barbados', 'America/Barbados'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('America/Whitehorse', 'America/Whitehorse'), ('US/Alaska', 'US/Alaska'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('US/Samoa', 'US/Samoa'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('America/Tijuana', 'America/Tijuana'), ('America/Atikokan', 'America/Atikokan'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Australia/Perth', 'Australia/Perth'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Africa/Bangui', 'Africa/Bangui'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Indian/Cocos', 'Indian/Cocos'), ('Egypt', 'Egypt'), ('America/Caracas', 'America/Caracas'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Asia/Tehran', 'Asia/Tehran'), ('Canada/Mountain', 'Canada/Mountain'), ('America/St_Thomas', 'America/St_Thomas'), ('America/Mazatlan', 'America/Mazatlan'), ('Pacific/Palau', 'Pacific/Palau'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Australia/North', 'Australia/North'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Marigot', 'America/Marigot'), ('Africa/Libreville', 'Africa/Libreville'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Monterrey', 'America/Monterrey'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Kuwait', 'Asia/Kuwait'), ('America/Denver', 'America/Denver'), ('America/Bahia', 'America/Bahia'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Omsk', 'Asia/Omsk'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Boa_Vista', 'America/Boa_Vista'), ('America/Lima', 'America/Lima'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Europe/London', 'Europe/London'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Boise', 'America/Boise'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Europe/Andorra', 'Europe/Andorra'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/Asuncion', 'America/Asuncion'), ('Etc/UCT', 'Etc/UCT'), ('Iran', 'Iran'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Indian/Comoro', 'Indian/Comoro'), ('Australia/Victoria', 'Australia/Victoria'), ('Africa/Lome', 'Africa/Lome'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Managua', 'America/Managua'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Montevideo', 'America/Montevideo'), ('Australia/NSW', 'Australia/NSW'), ('Greenwich', 'Greenwich'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/St_Lucia', 'America/St_Lucia'), ('Asia/Damascus', 'Asia/Damascus'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Virgin', 'America/Virgin'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Atka', 'America/Atka'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Navajo', 'Navajo'), ('Australia/ACT', 'Australia/ACT'), ('America/St_Vincent', 'America/St_Vincent'), ('GMT-0', 'GMT-0'), ('Indian/Reunion', 'Indian/Reunion'), ('Asia/Baghdad', 'Asia/Baghdad'), ('America/St_Kitts', 'America/St_Kitts'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Araguaina', 'America/Araguaina'), ('Australia/Hobart', 'Australia/Hobart'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Zulu', 'Zulu'), ('Turkey', 'Turkey'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Pacific/Ponape', 'Pacific/Ponape'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Resolute', 'America/Resolute'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Europe/Kirov', 'Europe/Kirov'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Paris', 'Europe/Paris'), ('Etc/GMT0', 'Etc/GMT0'), ('Africa/Bissau', 'Africa/Bissau'), ('Asia/Karachi', 'Asia/Karachi'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Africa/Lagos', 'Africa/Lagos'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Indian/Mahe', 'Indian/Mahe'), ('Etc/GMT', 'Etc/GMT'), ('America/Eirunepe', 'America/Eirunepe'), ('MET', 'MET'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Pacific/Guam', 'Pacific/Guam'), ('America/Yellowknife', 'America/Yellowknife'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Colombo', 'Asia/Colombo'), ('Africa/Douala', 'Africa/Douala'), ('America/Mendoza', 'America/Mendoza'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Anchorage', 'America/Anchorage'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Asia/Kabul', 'Asia/Kabul'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Indian/Maldives', 'Indian/Maldives'), ('Asia/Baku', 'Asia/Baku'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('America/Guyana', 'America/Guyana'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('US/Arizona', 'US/Arizona'), ('America/Regina', 'America/Regina'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Asia/Chita', 'Asia/Chita'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Guayaquil', 'America/Guayaquil'), ('CET', 'CET'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Universal', 'Universal'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Cayman', 'America/Cayman'), ('Asia/Harbin', 'Asia/Harbin'), ('Brazil/West', 'Brazil/West'), ('America/Dawson', 'America/Dawson'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Pacific/Niue', 'Pacific/Niue'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Africa/Niamey', 'Africa/Niamey'), ('Asia/Dacca', 'Asia/Dacca'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Asia/Yangon', 'Asia/Yangon'), ('Australia/Darwin', 'Australia/Darwin'), ('Indian/Christmas', 'Indian/Christmas'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Pacific/Wake', 'Pacific/Wake'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Canada/Pacific', 'Canada/Pacific'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/Santarem', 'America/Santarem'), ('Asia/Dubai', 'Asia/Dubai'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Australia/Currie', 'Australia/Currie'), ('Singapore', 'Singapore'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Adak', 'America/Adak'), ('Asia/Makassar', 'Asia/Makassar'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Africa/Asmara', 'Africa/Asmara'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Asia/Singapore', 'Asia/Singapore'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Europe/Tirane', 'Europe/Tirane'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('US/Eastern', 'US/Eastern'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Jujuy', 'America/Jujuy'), ('Canada/Eastern', 'Canada/Eastern'), ('Asia/Nicosia', 'Asia/Nicosia'), ('GB-Eire', 'GB-Eire'), ('Libya', 'Libya'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Nipigon', 'America/Nipigon'), ('America/Manaus', 'America/Manaus'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('America/Maceio', 'America/Maceio'), ('Jamaica', 'Jamaica'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Africa/Blantyre', 'Africa/Blantyre'), ('America/Montserrat', 'America/Montserrat'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Africa/Asmera', 'Africa/Asmera'), ('Australia/LHI', 'Australia/LHI'), ('Asia/Macao', 'Asia/Macao'), ('Iceland', 'Iceland'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Asia/Taipei', 'Asia/Taipei'), ('Europe/Saratov', 'Europe/Saratov'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('US/Central', 'US/Central'), ('Asia/Hovd', 'Asia/Hovd'), ('Pacific/Nauru', 'Pacific/Nauru'), ('EST5EDT', 'EST5EDT'), ('Australia/South', 'Australia/South'), ('America/Godthab', 'America/Godthab'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Europe/Monaco', 'Europe/Monaco'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('PST8PDT', 'PST8PDT'), ('America/Anguilla', 'America/Anguilla'), ('America/La_Paz', 'America/La_Paz'), ('Africa/Harare', 'Africa/Harare'), ('Hongkong', 'Hongkong'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('HST', 'HST'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('US/Pacific', 'US/Pacific'), ('America/Menominee', 'America/Menominee'), ('America/Phoenix', 'America/Phoenix'), ('Etc/GMT-9', 'Etc/GMT-9'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Brazil/East', 'Brazil/East'), ('Africa/Juba', 'Africa/Juba'), ('Europe/Skopje', 'Europe/Skopje'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Africa/Accra', 'Africa/Accra'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Asia/Kamchatka', 'Asia/Kamchatka')], default='UTC', max_length=50, verbose_name='Timezone')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Mailing launch date')),
                ('date_end', models.DateTimeField(verbose_name='Mailing end date')),
                ('message_text', models.TextField(max_length=255, verbose_name='Message text')),
                ('mobile_code', models.CharField(blank=True, max_length=3, verbose_name='Search by mobile operator code')),
                ('tags', models.CharField(blank=True, max_length=25, verbose_name='Search by tags')),
            ],
            options={
                'verbose_name': 'Mailing',
                'verbose_name_plural': 'Mailings',
                'ordering': ['date_end'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('failed', 'Failed'), ('active', 'Active')], max_length=7, verbose_name='Sending status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.mailing')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
