""" Some typing classes used both by FastAPI server and MongoDBA and others"""
from enum import Enum


class EmbassyCode(str, Enum):
    bj = 'bj'
    sh = 'sh'
    cd = 'cd'
    gz = 'gz'
    sy = 'sy'
    hk = 'hk'
    tp = 'tp'
    pp = 'pp'
    sg = 'sg'
    sel = 'sel'
    mel = 'mel'
    per = 'per'
    syd = 'syd'
    brn = 'brn'
    fuk = 'fuk'
    itm = 'itm'
    oka = 'oka'
    cts = 'cts'
    hnd = 'hnd'
    ktm = 'ktm'
    bkk = 'bkk'
    cnx = 'cnx'
    bfs = 'bfs'
    lcy = 'lcy'
    yyc = 'yyc'
    yhz = 'yhz'
    yul = 'yul'
    yow = 'yow'
    yqb = 'yqb'
    yyz = 'yyz'
    yvr = 'yvr'
    auh = 'auh'
    dxb = 'dxb'
    beg = 'beg'
    cdg = 'cdg'
    gye = 'gye'
    uio = 'uio'
    esb = 'esb'
    ist = 'ist'
    ath = 'ath'
    bog = 'bog'
    bgi = 'bgi'
    cjs = 'cjs'
    gdl = 'gdl'
    hmo = 'hmo'
    cvj = 'cvj'
    mid = 'mid'
    mex = 'mex'
    mty = 'mty'
    ols = 'ols'
    nld = 'nld'
    tij = 'tij'


class VisaType(str, Enum):
    F = 'F'
    B = 'B'
    H = 'H'
    O = 'O'  # noqa: E741
    L = 'L'


class System(str, Enum):
    CGI = 'cgi'
    AIS = 'ais'


class Region(str, Enum):
    SOUTH_EAST_ASIA = 'SOUTH_EAST_ASIA'
    EAST_ASIA = 'EAST_ASIA'
    WEST_ASIA = 'WEST_ASIA'
    SOUTH_ASIA = 'SOUTH_ASIA'
    OCEANIA = 'OCEANIA'
    WEST_EUROPE = 'WEST_EUROPE'
    EAST_EUROPE = 'EAST_EUROPE'
    NORTH_AMERICA = 'NORTH_AMERICA'
    SOUTH_AMERICA = 'SOUTH_AMERICA'


class Continent(str, Enum):
    ASIA = 'ASIA'
    OCEANIA = 'OCEANIA'
    EUROPE = 'EUROPE'
    NORTH_AMERICA = 'NORTH_AMERICA'
    SOUTH_AMERICA = 'SOUTH_AMERICA'


class Country(str, Enum):
    CHN = 'CHN'
    SGP = 'SGP'
    KHM = 'KHM'
    KOR = 'KOR'
    JPN = 'JPN'
    NPL = 'NPL'
    THA = 'THA'
    ARE = 'ARE'
    TUR = 'TUR'
    AUS = 'AUS'
    CHE = 'CHE'
    GBR = 'GBR'
    SRB = 'SRB'
    FRA = 'FRA'
    GRC = 'GRC'
    CAN = 'CAN'
    MEX = 'MEX'
    ECU = 'ECU'
    COL = 'COL'
    BRB = 'BRB'