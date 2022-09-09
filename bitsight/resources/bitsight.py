from enum import Enum

from bitsight.api_io.request_handler import RequestHandler


class BitSight:
    def __init__(self):
        self._handler = RequestHandler()
        self._BASE_URL = "https://api.bitsighttech.com/"

    def get(self, endpoint, **kwargs):
        """
        method for wrapping get requests and handling certain status codes
        :param endpoint: the url for the endpoint
        :return: response object
        """
        return self._handler.get(request_url=f"{self._BASE_URL}{endpoint}", **kwargs)

    def post(self, endpoint, json, **kwargs):
        """
        method for handling a post request
        :param json: the payload to post
        :param endpoint: the url for the endpoint
        :return: response object
        """
        return self._handler.post(
            request_url=f"{self._BASE_URL}{endpoint}", json=json, **kwargs
        )

    def delete(self, endpoint, **kwargs):
        """
        method for handling delete requests
        :param endpoint: the url to process for the DELETE request
        :return: response object with status code, text, etc.
        """
        return self._handler.delete(request_url=f"{self._BASE_URL}{endpoint}", **kwargs)

    def patch(self, endpoint, json, **kwargs):
        """
        method for handling a patch request
        :param json: the payload to patch
        :param endpoint: the url for the endpoint
        :return: response object
        """
        return self._handler.patch(
            request_url=f"{self._BASE_URL}{endpoint}", json=json, **kwargs
        )


class Endpoints:
    """
    Enumeration representing the available v1 and v2 endpoints
    """

    class V1(Enum):
        overview = ""
        enable_vendor_access = "access-requests/"
        companies = "companies/"
        company_relationships = "company-relationships/"
        company_requests = "company-requests/"
        customers = "customers/"
        defaults = "defaults/"
        exposed_credentials = "exposed-credentials/"
        wfh = "findings/wfh/"
        folders = "folders/"
        industries = "industries/"
        news = "news/"
        peer_analytics = "peer-analytics/"
        portfolio = "portfolio/"
        fast_ratings = "fast-ratings/"
        reports = "reports/"
        subscriptions = "subscriptions/"
        territories = "territories/"
        tiers = "tiers/"

        def __init__(self, path):
            self.path = path

        def __str__(self):
            return f"{self.__class__.__name__.lower()}/{self.path}"

        def __repr__(self):
            return f"{self.__class__.__name__.lower()}/{self.path}"

    class V2(Enum):
        overview = ""
        alerts = "alerts/"
        company_requests = "company-requests/"
        portfolio = "portfolio/"
        users = "users/"

        def __init__(self, path):
            self.path = path

        def __str__(self):
            return f"{self.__class__.__name__.lower()}/{self.path}"

        def __repr__(self):
            return f"{self.__class__.__name__.lower()}/{self.path}"


class Industries(Enum):
    """
    Enumeration representing the available industry names
    """

    aerospacedefense = "Aerospace/Defense"
    aviation_aerospace = "Aviation & Aerospace"
    defense_space = "Defense & Space"
    accounting = "Accounting"
    business_services = "Business Services"
    business_supplies_and_equipment = "Business Supplies and Equipment"
    consumer_services = "Consumer Services"
    design = "Design"
    environmental_services = "Environmental Services"
    events_services = "Events Services"
    executive_office = "Executive Office"
    facilities_services = "Facilities Services"
    graphic_design = "Graphic Design"
    human_resources = "Human Resources"
    import_and_export = "Import and Export"
    international_trade_and_development = "International Trade and Development"
    logistics_and_supply_chain = "Logistics and Supply Chain"
    management_consulting = "Management Consulting"
    market_research = "Market Research"
    marketing_and_advertising = "Marketing and Advertising"
    outsourcingoffshoring = "Outsourcing/Offshoring"
    photography = "Photography"
    printing = "Printing"
    professional_training_coaching = "Professional Training & Coaching"
    public_relations_and_communications = "Public Relations and Communications"
    public_safety = "Public Safety"
    security_and_investigations = "Security and Investigations"
    staffing_and_recruiting = "Staffing and Recruiting"
    translation_and_localization = "Translation and Localization"
    warehousing = "Warehousing"
    writing_and_editing = "Writing and Editing"
    apparel_fashion = "Apparel & Fashion"
    arts_and_crafts = "Arts and Crafts"
    consumer_goods = "Consumer Goods"
    cosmetics = "Cosmetics"
    luxury_goods_jewelry = "Luxury Goods & Jewelry"
    sporting_goods = "Sporting Goods"
    tobacco = "Tobacco"
    credit_union = "Credit Union"
    e_learning = "E-Learning"
    education = "Education"
    education_management = "Education Management"
    higher_education = "Higher Education"
    primarysecondary_education = "Primary/Secondary Education"
    research = "Research"
    energyresources = "Energy/Resources"
    mining_metals = "Mining & Metals"
    oil_energy = "Oil & Energy"
    paper_forest_products = "Paper & Forest Products"
    renewables_environment = "Renewables & Environment"
    architecture_planning = "Architecture & Planning"
    civil_engineering = "Civil Engineering"
    construction = "Construction"
    engineering = "Engineering"
    mechanical_or_industrial_engineering = "Mechanical or Industrial Engineering"
    banking = "Banking"
    capital_markets = "Capital Markets"
    finance = "Finance"
    financial_services = "Financial Services"
    investment_banking = "Investment Banking"
    investment_management = "Investment Management"
    venture_capital_private_equity = "Venture Capital & Private Equity"
    dairy = "Dairy"
    farming = "Farming"
    fishery = "Fishery"
    food_beverages = "Food & Beverages"
    food_production = "Food Production"
    ranching = "Ranching"
    wine_and_spirits = "Wine and Spirits"
    government_administration = "Government Administration"
    government_relations = "Government Relations"
    governmentpolitics = "Government/Politics"
    judiciary = "Judiciary"
    law_enforcement = "Law Enforcement"
    legislative_office = "Legislative Office"
    libraries = "Libraries"
    military = "Military"
    political_organization = "Political Organization"
    public_policy = "Public Policy"
    alternative_medicine = "Alternative Medicine"
    health_wellness_and_fitness = "Health, Wellness and Fitness"
    healthcarewellness = "Healthcare/Wellness"
    hospital_health_care = "Hospital & Health Care"
    medical_practice = "Medical Practice"
    mental_health_care = "Mental Health Care"
    pharmaceuticals = "Pharmaceuticals"
    veterinary = "Veterinary"
    insurance = "Insurance"
    alternative_dispute_resolution = "Alternative Dispute Resolution"
    law_practice = "Law Practice"
    legal = "Legal"
    legal_services = "Legal Services"
    building_materials = "Building Materials"
    chemicals = "Chemicals"
    electricalelectronic_manufacturing = "Electrical/Electronic Manufacturing"
    furniture = "Furniture"
    glass_ceramics_concrete = "Glass, Ceramics & Concrete"
    industrial_automation = "Industrial Automation"
    machinery = "Machinery"
    manufacturing = "Manufacturing"
    packaging_and_containers = "Packaging and Containers"
    plastics = "Plastics"
    railroad_manufacture = "Railroad Manufacture"
    shipbuilding = "Shipbuilding"
    textiles = "Textiles"
    animation = "Animation"
    broadcast_media = "Broadcast Media"
    entertainment = "Entertainment"
    media_production = "Media Production"
    mediaentertainment = "Media/Entertainment"
    motion_pictures_and_film = "Motion Pictures and Film"
    music = "Music"
    newspapers = "Newspapers"
    online_media = "Online Media"
    performing_arts = "Performing Arts"
    publishing = "Publishing"
    civic_social_organization = "Civic & Social Organization"
    fund_raising = "Fund-Raising"
    individual_family_services = "Individual & Family Services"
    international_affairs = "International Affairs"
    non_profit_organization_management = "Non-Profit Organization Management"
    nonprofitngo = "Nonprofit/NGO"
    philanthropy = "Philanthropy"
    program_development = "Program Development"
    religious_institutions = "Religious Institutions"
    think_tanks = "Think Tanks"
    commercial_real_estate = "Commercial Real Estate"
    real_estate = "Real Estate"
    fine_art = "Fine Art"
    retail = "Retail"
    supermarkets = "Supermarkets"
    wholesale = "Wholesale"
    biotechnology = "Biotechnology"
    computer_network_security = "Computer & Network Security"
    computer_games = "Computer Games"
    computer_hardware = "Computer Hardware"
    computer_networking = "Computer Networking"
    computer_software = "Computer Software"
    consumer_electronics = "Consumer Electronics"
    information_services = "Information Services"
    information_technology_and_services = "Information Technology and Services"
    internet = "Internet"
    medical_devices = "Medical Devices"
    nanotechnology = "Nanotechnology"
    semiconductors = "Semiconductors"
    technology = "Technology"
    wireless = "Wireless"
    telecommunications = "Telecommunications"
    gambling_casinos = "Gambling & Casinos"
    hospitality = "Hospitality"
    leisure_travel_tourism = "Leisure, Travel & Tourism"
    museums_and_institutions = "Museums and Institutions"
    recreational_facilities_and_services = "Recreational Facilities and Services"
    restaurants = "Restaurants"
    sports = "Sports"
    tourismhospitality = "Tourism/Hospitality"
    airlinesaviation = "Airlines/Aviation"
    automotive = "Automotive"
    maritime = "Maritime"
    packagefreight_delivery = "Package/Freight Delivery"
    transportation = "Transportation"
    utilities = "Utilities"

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class RiskVectors(Enum):
    """
    Enumeration representing the slugs for BitSight risk vectors for use with our api
    """

    botnet_infections = "botnet_infections"
    spam_propagation = "spam_propagation"
    malware_servers = "malware_servers"
    unsolicited_comm = "unsolicited_comm"
    potentially_exploited = "potentially_exploited"
    spf = "spf"
    dkim = "dkim"
    ssl_certificates = "ssl_certificates"
    ssl_configurations = "ssl_configurations"
    open_ports = "open_ports"
    dnssec = "dnssec"
    application_security = "application_security"
    patching_cadence = "patching_cadence"
    insecure_systems = "insecure_systems"
    server_software = "server_software"
    desktop_software = "desktop_software"
    mobile_software = "mobile_software"
    mobile_application_security = "mobile_application_security"
    data_breaches = "data_breaches"
    exposed_credentials = "exposed_credentials"
    file_sharing = "file_sharing"

    def __init__(self, risk_vector_slug):
        self.risk_vector_slug = risk_vector_slug

    def __str__(self):
        return f"{self.risk_vector_slug}"

    def __repr__(self):
        return f"{self.risk_vector_slug}"


class Severity(Enum):
    """
    Enumeration representing the BitSight finding severity values
    """

    minor = "minor"
    moderate = "moderate"
    material = "material"
    severe = "severe"

    def __init__(self, severity_slug):
        self.severity_slug = severity_slug

    def __str__(self):
        return f"{self.severity_slug}"

    def __repr__(self):
        return f"{self.severity_slug}"


class FindingGrade(Enum):
    """
    Enumeration representing the BitSight finding grade values
    """

    good = "good"
    fair = "fair"
    warn = "warn"
    bad = "bad"
    neutral = "neutral"
    na = "na"

    def __init__(self, grade_slug):
        self.grade_slug = grade_slug

    def __str__(self):
        return f"{self.grade_slug}"

    def __repr__(self):
        return f"{self.grade_slug}"


class AssetImportance(Enum):
    """
    Enumeration representing the BitSight asset importance values
    """

    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"
    null = "null"

    def __init__(self, importance_slug):
        self.importance_slug = importance_slug

    def __str__(self):
        return f"{self.importance_slug}"

    def __repr__(self):
        return f"{self.importance_slug}"


class LicenseType(Enum):
    """
    Enumeration representing the BitSight licence types
    """

    alerts_only = "alerts-only"
    applicants = "applicants"
    continuous_monitoring = "continuous_monitoring"
    countries = "countries"
    insureds = "continuous_monitoring"
    my_subsidiary = "my_subsidiary"
    one_time = "one-time"
    vendor_selection = "vendor-selection"

    def __init__(self, license_slug):
        self.license_slug = license_slug

    def __str__(self):
        return f"{self.license_slug}"

    def __repr__(self):
        return f"{self.license_slug}"
