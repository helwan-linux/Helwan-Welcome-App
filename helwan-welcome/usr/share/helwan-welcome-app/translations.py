#!/usr/bin/env python3
# CREATED BY Saeed Badrelden <saeedbadrelden2021@gmail.com>

import os
import sys
import gettext

def load_translation(language_code):

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    # المسار الصحيح لمجلد locales داخل helwan-welcome-app
    locale_path = os.path.join(base_path, 'locales')

    try:
        translation = gettext.translation('base', localedir=locale_path, languages=[language_code])
        translation.install()
        return translation.gettext
    except FileNotFoundError:
        print(f"[!] Translation not found for {language_code} in {locale_path}")
        return lambda s: s



DEFAULT_LANGUAGE_CODE = 'en'
_ = load_translation(DEFAULT_LANGUAGE_CODE)

# قائمة بلغات النظام المدعومة مع الأسماء المقابلة
SYSTEM_LANGUAGES = languages = {
	'ar_EG.UTF-8': 'العربية (مصر)',
	'en_US.UTF-8': 'English (US)',
	'es_ES.UTF-8': 'Español (España)',
	'pt_PT.UTF-8': 'Português (Portugal)',
	'de_DE.UTF-8': 'Deutsch (Deutschland)',
	'fr_FR.UTF-8': 'Français (France)',
	'ru_RU.UTF-8': 'Русский (Россия)',
	'zh_CN.UTF-8': '中文 (简体)',
	'ja_JP.UTF-8': '日本語',
	'it_IT.UTF-8': 'Italiano',
	'pl_PL.UTF-8': 'Polski',
	'ro_RO.UTF-8': 'Română',
	'ur_PK.UTF-8': 'اردو',
	'fa_IR.UTF-8': 'فارسی',
	'hu_HU.UTF-8': 'Magyar',
	'da_DK.UTF-8': 'Dansk (Danmark)',
	'sv_SE.UTF-8': 'Svenska (Sverige)',
	'hi_HI.UTF-8': 'हिन्दी (भारत)',

	'bn_BD.UTF-8': 'বাংলা (বাংলাদেশ)',
	'ta_IN.UTF-8': 'தமிழ் (இந்தியா)',
	'tr_TR.UTF-8': 'Türkçe (Türkiye)',
	'id_ID.UTF-8': 'Bahasa Indonesia',
	'ko_KR.UTF-8': '한국어 (대한민국)',
	'fil_PH.UTF-8': 'Filipino (Pilipinas)',
	'vi_VN.UTF-8': 'Tiếng Việt (Việt Nam)',
	'uk_UA.UTF-8': 'Українська (Україна)',
	'nl_NL.UTF-8': 'Nederlands (Nederland)',
	'nb_NO.UTF-8': 'Norsk (Norge)',
	'fi_FI.UTF-8': 'Suomi (Suomi)',
	'th_TH.UTF-8': 'ไทย (ประเทศไทย)',
	'bg_BG.UTF-8': 'Български (България)',
	'he_IL.UTF-8': 'עברית (ישראל)',

	'ca_ES.UTF-8': 'Català (Espanya)',
	'lv_LV.UTF-8': 'Latviešu (Latvija)',
	'sr_RS.UTF-8': 'Српски (Србија)',
	'sk_SK.UTF-8': 'Slovenčina (Slovensko)',
	'mt_MT.UTF-8': 'Malti (Malta)',
	'sq_AL.UTF-8': 'Shqip (Shqipëri)',
	'mn_MN.UTF-8': 'Монгол (Монгол)',
}

# قائمة لغة التطبيق بنفس الطريقة
APP_LANGUAGES = languages = {
	'ar_EG.UTF-8': 'العربية (مصر)',
	'en_US.UTF-8': 'English (US)',
	'es_ES.UTF-8': 'Español (España)',
	'pt_PT.UTF-8': 'Português (Portugal)',
	'de_DE.UTF-8': 'Deutsch (Deutschland)',
	'fr_FR.UTF-8': 'Français (France)',
	'ru_RU.UTF-8': 'Русский (Россия)',
	'zh_CN.UTF-8': '中文 (简体)',
	'ja_JP.UTF-8': '日本語',
	'it_IT.UTF-8': 'Italiano',
	'pl_PL.UTF-8': 'Polski',
	'ro_RO.UTF-8': 'Română',
	'ur_PK.UTF-8': 'اردو',
	'fa_IR.UTF-8': 'فارسی',
	'hu_HU.UTF-8': 'Magyar',
	'da_DK.UTF-8': 'Dansk (Danmark)',
	'sv_SE.UTF-8': 'Svenska (Sverige)',
	'hi_HI.UTF-8': 'हिन्दी (भारत)',

	'bn_BD.UTF-8': 'বাংলা (বাংলাদেশ)',
	'ta_IN.UTF-8': 'தமிழ் (இந்தியா)',
	'tr_TR.UTF-8': 'Türkçe (Türkiye)',
	'id_ID.UTF-8': 'Bahasa Indonesia',
	'ko_KR.UTF-8': '한국어 (대한민국)',
	'fil_PH.UTF-8': 'Filipino (Pilipinas)',
	'vi_VN.UTF-8': 'Tiếng Việt (Việt Nam)',
	'uk_UA.UTF-8': 'Українська (Україна)',
	'nl_NL.UTF-8': 'Nederlands (Nederland)',
	'nb_NO.UTF-8': 'Norsk (Norge)',
	'fi_FI.UTF-8': 'Suomi (Suomi)',
	'th_TH.UTF-8': 'ไทย (ประเทศไทย)',
	'bg_BG.UTF-8': 'Български (България)',
	'he_IL.UTF-8': 'עברית (ישראל)',

	'ca_ES.UTF-8': 'Català (Espanya)',
	'lv_LV.UTF-8': 'Latviešu (Latvija)',
	'sr_RS.UTF-8': 'Српски (Србија)',
	'sk_SK.UTF-8': 'Slovenčina (Slovensko)',
	'mt_MT.UTF-8': 'Malti (Malta)',
	'sq_AL.UTF-8': 'Shqip (Shqipëri)',
	'mn_MN.UTF-8': 'Монгол (Монгол)',
}
