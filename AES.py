from tkinter import W

rowLimit = 4;
roundKeyLimit = 12;
colsPerKey = 4;

sbox = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"], 
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"], 
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"], 
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"], 
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"], 
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"], 
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"], 
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"], 
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"], 
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"], 
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"], 
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"], 
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"], 
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"], 
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"], 
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

sboxInv = [
    ["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"], 
    ["7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb"], 
    ["54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"], 
    ["08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25"], 
    ["72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"], 
    ["6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84"], 
    ["90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06"], 
    ["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b"], 
    ["3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"], 
    ["96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e"], 
    ["47", "f1", "1a", "71", "1d", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b"], 
    ["fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"], 
    ["1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f"], 
    ["60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"], 
    ["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61"], 
    ["17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]
]

rcon = [
    "8D", "01", "02", "04", "08", "10", "20", "40", "80", "1B", "36", "6C", "D8", "AB", "4D", "9A", 
    "2F", "5E", "BC", "63", "C6", "97", "35", "6A", "D4", "B3", "7D", "FA", "EF", "C5", "91", "39", 
    "72", "E4", "D3", "BD", "61", "C2", "9F", "25", "4A", "94", "33", "66", "CC", "83", "1D", "3A", 
    "74", "E8", "CB", "8D", "01", "02", "04", "08", "10", "20", "40", "80", "1B", "36", "6C", "D8", 
    "AB", "4D", "9A", "2F", "5E", "BC", "63", "C6", "97", "35", "6A", "D4", "B3", "7D", "FA", "EF", 
    "C5", "91", "39", "72", "E4", "D3", "BD", "61", "C2", "9F", "25", "4A", "94", "33", "66", "CC", 
    "83", "1D", "3A", "74", "E8", "CB", "8D", "01", "02", "04", "08", "10", "20", "40", "80", "1B", 
    "36", "6C", "D8", "AB", "4D", "9A", "2F", "5E", "BC", "63", "C6", "97", "35", "6A", "D4", "B3", 
    "7D", "FA", "EF", "C5", "91", "39", "72", "E4", "D3", "BD", "61", "C2", "9F", "25", "4A", "94", 
    "33", "66", "CC", "83", "1D", "3A", "74", "E8", "CB", "8D", "01", "02", "04", "08", "10", "20", 
    "40", "80", "1B", "36", "6C", "D8", "AB", "4D", "9A", "2F", "5E", "BC", "63", "C6", "97", "35", 
    "6A", "D4", "B3", "7D", "FA", "EF", "C5", "91", "39", "72", "E4", "D3", "BD", "61", "C2", "9F", 
    "25", "4A", "94", "33", "66", "CC", "83", "1D", "3A", "74", "E8", "CB", "8D", "01", "02", "04", 
    "08", "10", "20", "40", "80", "1B", "36", "6C", "D8", "AB", "4D", "9A", "2F", "5E", "BC", "63", 
    "C6", "97", "35", "6A", "D4", "B3", "7D", "FA", "EF", "C5", "91", "39", "72", "E4", "D3", "BD", 
    "61", "C2", "9F", "25", "4A", "94", "33", "66", "CC", "83", "1D", "3A", "74", "E8", "CB", "8D"
]

mult2 = [
    ["0x00", "0x02", "0x04", "0x06", "0x08", "0x0a", "0x0c", "0x0e", "0x10", "0x12", "0x14", "0x16", "0x18", "0x1a", "0x1c", "0x1e"], 
    ["0x20", "0x22", "0x24", "0x26", "0x28", "0x2a", "0x2c", "0x2e", "0x30", "0x32", "0x34", "0x36", "0x38", "0x3a", "0x3c", "0x3e"], 
    ["0x40", "0x42", "0x44", "0x46", "0x48", "0x4a", "0x4c", "0x4e", "0x50", "0x52", "0x54", "0x56", "0x58", "0x5a", "0x5c", "0x5e"], 
    ["0x60", "0x62", "0x64", "0x66", "0x68", "0x6a", "0x6c", "0x6e", "0x70", "0x72", "0x74", "0x76", "0x78", "0x7a", "0x7c", "0x7e"], 
    ["0x80", "0x82", "0x84", "0x86", "0x88", "0x8a", "0x8c", "0x8e", "0x90", "0x92", "0x94", "0x96", "0x98", "0x9a", "0x9c", "0x9e"], 
    ["0xa0", "0xa2", "0xa4", "0xa6", "0xa8", "0xaa", "0xac", "0xae", "0xb0", "0xb2", "0xb4", "0xb6", "0xb8", "0xba", "0xbc", "0xbe"], 
    ["0xc0", "0xc2", "0xc4", "0xc6", "0xc8", "0xca", "0xcc", "0xce", "0xd0", "0xd2", "0xd4", "0xd6", "0xd8", "0xda", "0xdc", "0xde"], 
    ["0xe0", "0xe2", "0xe4", "0xe6", "0xe8", "0xea", "0xec", "0xee", "0xf0", "0xf2", "0xf4", "0xf6", "0xf8", "0xfa", "0xfc", "0xfe"], 
    ["0x1b", "0x19", "0x1f", "0x1d", "0x13", "0x11", "0x17", "0x15", "0x0b", "0x09", "0x0f", "0x0d", "0x03", "0x01", "0x07", "0x05"], 
    ["0x3b", "0x39", "0x3f", "0x3d", "0x33", "0x31", "0x37", "0x35", "0x2b", "0x29", "0x2f", "0x2d", "0x23", "0x21", "0x27", "0x25"], 
    ["0x5b", "0x59", "0x5f", "0x5d", "0x53", "0x51", "0x57", "0x55", "0x4b", "0x49", "0x4f", "0x4d", "0x43", "0x41", "0x47", "0x45"], 
    ["0x7b", "0x79", "0x7f", "0x7d", "0x73", "0x71", "0x77", "0x75", "0x6b", "0x69", "0x6f", "0x6d", "0x63", "0x61", "0x67", "0x65"], 
    ["0x9b", "0x99", "0x9f", "0x9d", "0x93", "0x91", "0x97", "0x95", "0x8b", "0x89", "0x8f", "0x8d", "0x83", "0x81", "0x87", "0x85"], 
    ["0xbb", "0xb9", "0xbf", "0xbd", "0xb3", "0xb1", "0xb7", "0xb5", "0xab", "0xa9", "0xaf", "0xad", "0xa3", "0xa1", "0xa7", "0xa5"], 
    ["0xdb", "0xd9", "0xdf", "0xdd", "0xd3", "0xd1", "0xd7", "0xd5", "0xcb", "0xc9", "0xcf", "0xcd", "0xc3", "0xc1", "0xc7", "0xc5"], 
    ["0xfb", "0xf9", "0xff", "0xfd", "0xf3", "0xf1", "0xf7", "0xf5", "0xeb", "0xe9", "0xef", "0xed", "0xe3", "0xe1", "0xe7", "0xe5"]
]

mult3 = [
    ["0x00", "0x03", "0x06", "0x05", "0x0c", "0x0f", "0x0a", "0x09", "0x18", "0x1b", "0x1e", "0x1d", "0x14", "0x17", "0x12", "0x11"], 
    ["0x30", "0x33", "0x36", "0x35", "0x3c", "0x3f", "0x3a", "0x39", "0x28", "0x2b", "0x2e", "0x2d", "0x24", "0x27", "0x22", "0x21"], 
    ["0x60", "0x63", "0x66", "0x65", "0x6c", "0x6f", "0x6a", "0x69", "0x78", "0x7b", "0x7e", "0x7d", "0x74", "0x77", "0x72", "0x71"], 
    ["0x50", "0x53", "0x56", "0x55", "0x5c", "0x5f", "0x5a", "0x59", "0x48", "0x4b", "0x4e", "0x4d", "0x44", "0x47", "0x42", "0x41"], 
    ["0xc0", "0xc3", "0xc6", "0xc5", "0xcc", "0xcf", "0xca", "0xc9", "0xd8", "0xdb", "0xde", "0xdd", "0xd4", "0xd7", "0xd2", "0xd1"], 
    ["0xf0", "0xf3", "0xf6", "0xf5", "0xfc", "0xff", "0xfa", "0xf9", "0xe8", "0xeb", "0xee", "0xed", "0xe4", "0xe7", "0xe2", "0xe1"], 
    ["0xa0", "0xa3", "0xa6", "0xa5", "0xac", "0xaf", "0xaa", "0xa9", "0xb8", "0xbb", "0xbe", "0xbd", "0xb4", "0xb7", "0xb2", "0xb1"], 
    ["0x90", "0x93", "0x96", "0x95", "0x9c", "0x9f", "0x9a", "0x99", "0x88", "0x8b", "0x8e", "0x8d", "0x84", "0x87", "0x82", "0x81"], 
    ["0x9b", "0x98", "0x9d", "0x9e", "0x97", "0x94", "0x91", "0x92", "0x83", "0x80", "0x85", "0x86", "0x8f", "0x8c", "0x89", "0x8a"], 
    ["0xab", "0xa8", "0xad", "0xae", "0xa7", "0xa4", "0xa1", "0xa2", "0xb3", "0xb0", "0xb5", "0xb6", "0xbf", "0xbc", "0xb9", "0xba"], 
    ["0xfb", "0xf8", "0xfd", "0xfe", "0xf7", "0xf4", "0xf1", "0xf2", "0xe3", "0xe0", "0xe5", "0xe6", "0xef", "0xec", "0xe9", "0xea"], 
    ["0xcb", "0xc8", "0xcd", "0xce", "0xc7", "0xc4", "0xc1", "0xc2", "0xd3", "0xd0", "0xd5", "0xd6", "0xdf", "0xdc", "0xd9", "0xda"], 
    ["0x5b", "0x58", "0x5d", "0x5e", "0x57", "0x54", "0x51", "0x52", "0x43", "0x40", "0x45", "0x46", "0x4f", "0x4c", "0x49", "0x4a"], 
    ["0x6b", "0x68", "0x6d", "0x6e", "0x67", "0x64", "0x61", "0x62", "0x73", "0x70", "0x75", "0x76", "0x7f", "0x7c", "0x79", "0x7a"], 
    ["0x3b", "0x38", "0x3d", "0x3e", "0x37", "0x34", "0x31", "0x32", "0x23", "0x20", "0x25", "0x26", "0x2f", "0x2c", "0x29", "0x2a"], 
    ["0x0b", "0x08", "0x0d", "0x0e", "0x07", "0x04", "0x01", "0x02", "0x13", "0x10", "0x15", "0x16", "0x1f", "0x1c", "0x19", "0x1a"]
]

mult9 = [
    ["0x00", "0x09", "0x12", "0x1b", "0x24", "0x2d", "0x36", "0x3f", "0x48", "0x41", "0x5a", "0x53", "0x6c", "0x65", "0x7e", "0x77"], 
    ["0x90", "0x99", "0x82", "0x8b", "0xb4", "0xbd", "0xa6", "0xaf", "0xd8", "0xd1", "0xca", "0xc3", "0xfc", "0xf5", "0xee", "0xe7"], 
    ["0x3b", "0x32", "0x29", "0x20", "0x1f", "0x16", "0x0d", "0x04", "0x73", "0x7a", "0x61", "0x68", "0x57", "0x5e", "0x45", "0x4c"], 
    ["0xab", "0xa2", "0xb9", "0xb0", "0x8f", "0x86", "0x9d", "0x94", "0xe3", "0xea", "0xf1", "0xf8", "0xc7", "0xce", "0xd5", "0xdc"], 
    ["0x76", "0x7f", "0x64", "0x6d", "0x52", "0x5b", "0x40", "0x49", "0x3e", "0x37", "0x2c", "0x25", "0x1a", "0x13", "0x08", "0x01"], 
    ["0xe6", "0xef", "0xf4", "0xfd", "0xc2", "0xcb", "0xd0", "0xd9", "0xae", "0xa7", "0xbc", "0xb5", "0x8a", "0x83", "0x98", "0x91"], 
    ["0x4d", "0x44", "0x5f", "0x56", "0x69", "0x60", "0x7b", "0x72", "0x05", "0x0c", "0x17", "0x1e", "0x21", "0x28", "0x33", "0x3a"], 
    ["0xdd", "0xd4", "0xcf", "0xc6", "0xf9", "0xf0", "0xeb", "0xe2", "0x95", "0x9c", "0x87", "0x8e", "0xb1", "0xb8", "0xa3", "0xaa"], 
    ["0xec", "0xe5", "0xfe", "0xf7", "0xc8", "0xc1", "0xda", "0xd3", "0xa4", "0xad", "0xb6", "0xbf", "0x80", "0x89", "0x92", "0x9b"], 
    ["0x7c", "0x75", "0x6e", "0x67", "0x58", "0x51", "0x4a", "0x43", "0x34", "0x3d", "0x26", "0x2f", "0x10", "0x19", "0x02", "0x0b"], 
    ["0xd7", "0xde", "0xc5", "0xcc", "0xf3", "0xfa", "0xe1", "0xe8", "0x9f", "0x96", "0x8d", "0x84", "0xbb", "0xb2", "0xa9", "0xa0"], 
    ["0x47", "0x4e", "0x55", "0x5c", "0x63", "0x6a", "0x71", "0x78", "0x0f", "0x06", "0x1d", "0x14", "0x2b", "0x22", "0x39", "0x30"], 
    ["0x9a", "0x93", "0x88", "0x81", "0xbe", "0xb7", "0xac", "0xa5", "0xd2", "0xdb", "0xc0", "0xc9", "0xf6", "0xff", "0xe4", "0xed"], 
    ["0x0a", "0x03", "0x18", "0x11", "0x2e", "0x27", "0x3c", "0x35", "0x42", "0x4b", "0x50", "0x59", "0x66", "0x6f", "0x74", "0x7d"], 
    ["0xa1", "0xa8", "0xb3", "0xba", "0x85", "0x8c", "0x97", "0x9e", "0xe9", "0xe0", "0xfb", "0xf2", "0xcd", "0xc4", "0xdf", "0xd6"], 
    ["0x31", "0x38", "0x23", "0x2a", "0x15", "0x1c", "0x07", "0x0e", "0x79", "0x70", "0x6b", "0x62", "0x5d", "0x54", "0x4f", "0x46"]
]

mult11 = [
    ["0x00", "0x0b", "0x16", "0x1d", "0x2c", "0x27", "0x3a", "0x31", "0x58", "0x53", "0x4e", "0x45", "0x74", "0x7f", "0x62", "0x69"], 
    ["0xb0", "0xbb", "0xa6", "0xad", "0x9c", "0x97", "0x8a", "0x81", "0xe8", "0xe3", "0xfe", "0xf5", "0xc4", "0xcf", "0xd2", "0xd9"], 
    ["0x7b", "0x70", "0x6d", "0x66", "0x57", "0x5c", "0x41", "0x4a", "0x23", "0x28", "0x35", "0x3e", "0x0f", "0x04", "0x19", "0x12"], 
    ["0xcb", "0xc0", "0xdd", "0xd6", "0xe7", "0xec", "0xf1", "0xfa", "0x93", "0x98", "0x85", "0x8e", "0xbf", "0xb4", "0xa9", "0xa2"], 
    ["0xf6", "0xfd", "0xe0", "0xeb", "0xda", "0xd1", "0xcc", "0xc7", "0xae", "0xa5", "0xb8", "0xb3", "0x82", "0x89", "0x94", "0x9f"], 
    ["0x46", "0x4d", "0x50", "0x5b", "0x6a", "0x61", "0x7c", "0x77", "0x1e", "0x15", "0x08", "0x03", "0x32", "0x39", "0x24", "0x2f"], 
    ["0x8d", "0x86", "0x9b", "0x90", "0xa1", "0xaa", "0xb7", "0xbc", "0xd5", "0xde", "0xc3", "0xc8", "0xf9", "0xf2", "0xef", "0xe4"], 
    ["0x3d", "0x36", "0x2b", "0x20", "0x11", "0x1a", "0x07", "0x0c", "0x65", "0x6e", "0x73", "0x78", "0x49", "0x42", "0x5f", "0x54"], 
    ["0xf7", "0xfc", "0xe1", "0xea", "0xdb", "0xd0", "0xcd", "0xc6", "0xaf", "0xa4", "0xb9", "0xb2", "0x83", "0x88", "0x95", "0x9e"], 
    ["0x47", "0x4c", "0x51", "0x5a", "0x6b", "0x60", "0x7d", "0x76", "0x1f", "0x14", "0x09", "0x02", "0x33", "0x38", "0x25", "0x2e"], 
    ["0x8c", "0x87", "0x9a", "0x91", "0xa0", "0xab", "0xb6", "0xbd", "0xd4", "0xdf", "0xc2", "0xc9", "0xf8", "0xf3", "0xee", "0xe5"], 
    ["0x3c", "0x37", "0x2a", "0x21", "0x10", "0x1b", "0x06", "0x0d", "0x64", "0x6f", "0x72", "0x79", "0x48", "0x43", "0x5e", "0x55"], 
    ["0x01", "0x0a", "0x17", "0x1c", "0x2d", "0x26", "0x3b", "0x30", "0x59", "0x52", "0x4f", "0x44", "0x75", "0x7e", "0x63", "0x68"], 
    ["0xb1", "0xba", "0xa7", "0xac", "0x9d", "0x96", "0x8b", "0x80", "0xe9", "0xe2", "0xff", "0xf4", "0xc5", "0xce", "0xd3", "0xd8"], 
    ["0x7a", "0x71", "0x6c", "0x67", "0x56", "0x5d", "0x40", "0x4b", "0x22", "0x29", "0x34", "0x3f", "0x0e", "0x05", "0x18", "0x13"], 
    ["0xca", "0xc1", "0xdc", "0xd7", "0xe6", "0xed", "0xf0", "0xfb", "0x92", "0x99", "0x84", "0x8f", "0xbe", "0xb5", "0xa8", "0xa3"]
]

mult13 = [
    ["0x00", "0x0d", "0x1a", "0x17", "0x34", "0x39", "0x2e", "0x23", "0x68", "0x65", "0x72", "0x7f", "0x5c", "0x51", "0x46", "0x4b"], 
    ["0xd0", "0xdd", "0xca", "0xc7", "0xe4", "0xe9", "0xfe", "0xf3", "0xb8", "0xb5", "0xa2", "0xaf", "0x8c", "0x81", "0x96", "0x9b"], 
    ["0xbb", "0xb6", "0xa1", "0xac", "0x8f", "0x82", "0x95", "0x98", "0xd3", "0xde", "0xc9", "0xc4", "0xe7", "0xea", "0xfd", "0xf0"], 
    ["0x6b", "0x66", "0x71", "0x7c", "0x5f", "0x52", "0x45", "0x48", "0x03", "0x0e", "0x19", "0x14", "0x37", "0x3a", "0x2d", "0x20"], 
    ["0x6d", "0x60", "0x77", "0x7a", "0x59", "0x54", "0x43", "0x4e", "0x05", "0x08", "0x1f", "0x12", "0x31", "0x3c", "0x2b", "0x26"], 
    ["0xbd", "0xb0", "0xa7", "0xaa", "0x89", "0x84", "0x93", "0x9e", "0xd5", "0xd8", "0xcf", "0xc2", "0xe1", "0xec", "0xfb", "0xf6"], 
    ["0xd6", "0xdb", "0xcc", "0xc1", "0xe2", "0xef", "0xf8", "0xf5", "0xbe", "0xb3", "0xa4", "0xa9", "0x8a", "0x87", "0x90", "0x9d"], 
    ["0x06", "0x0b", "0x1c", "0x11", "0x32", "0x3f", "0x28", "0x25", "0x6e", "0x63", "0x74", "0x79", "0x5a", "0x57", "0x40", "0x4d"], 
    ["0xda", "0xd7", "0xc0", "0xcd", "0xee", "0xe3", "0xf4", "0xf9", "0xb2", "0xbf", "0xa8", "0xa5", "0x86", "0x8b", "0x9c", "0x91"], 
    ["0x0a", "0x07", "0x10", "0x1d", "0x3e", "0x33", "0x24", "0x29", "0x62", "0x6f", "0x78", "0x75", "0x56", "0x5b", "0x4c", "0x41"], 
    ["0x61", "0x6c", "0x7b", "0x76", "0x55", "0x58", "0x4f", "0x42", "0x09", "0x04", "0x13", "0x1e", "0x3d", "0x30", "0x27", "0x2a"], 
    ["0xb1", "0xbc", "0xab", "0xa6", "0x85", "0x88", "0x9f", "0x92", "0xd9", "0xd4", "0xc3", "0xce", "0xed", "0xe0", "0xf7", "0xfa"], 
    ["0xb7", "0xba", "0xad", "0xa0", "0x83", "0x8e", "0x99", "0x94", "0xdf", "0xd2", "0xc5", "0xc8", "0xeb", "0xe6", "0xf1", "0xfc"], 
    ["0x67", "0x6a", "0x7d", "0x70", "0x53", "0x5e", "0x49", "0x44", "0x0f", "0x02", "0x15", "0x18", "0x3b", "0x36", "0x21", "0x2c"], 
    ["0x0c", "0x01", "0x16", "0x1b", "0x38", "0x35", "0x22", "0x2f", "0x64", "0x69", "0x7e", "0x73", "0x50", "0x5d", "0x4a", "0x47"], 
    ["0xdc", "0xd1", "0xc6", "0xcb", "0xe8", "0xe5", "0xf2", "0xff", "0xb4", "0xb9", "0xae", "0xa3", "0x80", "0x8d", "0x9a", "0x97"]
]

mult14 = [
    ["0x00", "0x0e", "0x1c", "0x12", "0x38", "0x36", "0x24", "0x2a", "0x70", "0x7e", "0x6c", "0x62", "0x48", "0x46", "0x54", "0x5a"], 
    ["0xe0", "0xee", "0xfc", "0xf2", "0xd8", "0xd6", "0xc4", "0xca", "0x90", "0x9e", "0x8c", "0x82", "0xa8", "0xa6", "0xb4", "0xba"], 
    ["0xdb", "0xd5", "0xc7", "0xc9", "0xe3", "0xed", "0xff", "0xf1", "0xab", "0xa5", "0xb7", "0xb9", "0x93", "0x9d", "0x8f", "0x81"], 
    ["0x3b", "0x35", "0x27", "0x29", "0x03", "0x0d", "0x1f", "0x11", "0x4b", "0x45", "0x57", "0x59", "0x73", "0x7d", "0x6f", "0x61"], 
    ["0xad", "0xa3", "0xb1", "0xbf", "0x95", "0x9b", "0x89", "0x87", "0xdd", "0xd3", "0xc1", "0xcf", "0xe5", "0xeb", "0xf9", "0xf7"], 
    ["0x4d", "0x43", "0x51", "0x5f", "0x75", "0x7b", "0x69", "0x67", "0x3d", "0x33", "0x21", "0x2f", "0x05", "0x0b", "0x19", "0x17"], 
    ["0x76", "0x78", "0x6a", "0x64", "0x4e", "0x40", "0x52", "0x5c", "0x06", "0x08", "0x1a", "0x14", "0x3e", "0x30", "0x22", "0x2c"], 
    ["0x96", "0x98", "0x8a", "0x84", "0xae", "0xa0", "0xb2", "0xbc", "0xe6", "0xe8", "0xfa", "0xf4", "0xde", "0xd0", "0xc2", "0xcc"], 
    ["0x41", "0x4f", "0x5d", "0x53", "0x79", "0x77", "0x65", "0x6b", "0x31", "0x3f", "0x2d", "0x23", "0x09", "0x07", "0x15", "0x1b"], 
    ["0xa1", "0xaf", "0xbd", "0xb3", "0x99", "0x97", "0x85", "0x8b", "0xd1", "0xdf", "0xcd", "0xc3", "0xe9", "0xe7", "0xf5", "0xfb"], 
    ["0x9a", "0x94", "0x86", "0x88", "0xa2", "0xac", "0xbe", "0xb0", "0xea", "0xe4", "0xf6", "0xf8", "0xd2", "0xdc", "0xce", "0xc0"], 
    ["0x7a", "0x74", "0x66", "0x68", "0x42", "0x4c", "0x5e", "0x50", "0x0a", "0x04", "0x16", "0x18", "0x32", "0x3c", "0x2e", "0x20"], 
    ["0xec", "0xe2", "0xf0", "0xfe", "0xd4", "0xda", "0xc8", "0xc6", "0x9c", "0x92", "0x80", "0x8e", "0xa4", "0xaa", "0xb8", "0xb6"], 
    ["0x0c", "0x02", "0x10", "0x1e", "0x34", "0x3a", "0x28", "0x26", "0x7c", "0x72", "0x60", "0x6e", "0x44", "0x4a", "0x58", "0x56"], 
    ["0x37", "0x39", "0x2b", "0x25", "0x0f", "0x01", "0x13", "0x1d", "0x47", "0x49", "0x5b", "0x55", "0x7f", "0x71", "0x63", "0x6d"], 
    ["0xd7", "0xd9", "0xcb", "0xc5", "0xef", "0xe1", "0xf3", "0xfd", "0xa7", "0xa9", "0xbb", "0xb5", "0x9f", "0x91", "0x83", "0x8d"]
]

mixCols = [
    ["02", "03", "01", "01"], 
    ["01", "02", "03", "01"], 
    ["01", "01", "02", "03"], 
    ["03", "01", "01", "02"]
]

invMixCols = [
    ["0E", "0B", "0D", "09"], 
    ["09", "0E", "0B", "0D"], 
    ["0D", "09", "0E", "0B"], 
    ["0B", "0D", "09", "0E"]
]

def aesSBox(inHex):
    # the input must first be broken up into the row and column
    # that will be pointed to
    row = int("" + inHex[0], 16)
    col = int("" + inHex[1], 16)
    return sbox[row][col]

def sBoxInverse(inHex):
    # the input must first be broken up into the row and column
    # that will be pointed to
    row = int("" + inHex[0], 16)
    col = int("" + inHex[1], 16)
    return sboxInv[row][col]

def aesRcon(round):
    return rcon[round];

# *
#   * toByteMatrix
#   *
#   * Coverts the string of values into a matrix of bytes(represented by strings)
#   * in column major order
#   *
#   * @param input: inputted string that is being turned into a matrix
#   * @return: matrix of bytes
def toByteMatrix(input):
    W = [[0] * 44 for i in range(4)]

    if len(input) < 32:
        while len(input) != 32:
            input = input + "20"

    # Insert the input-string values into matrix W in column-major order
    step = 0
    r = 0
    rowLimit = len(W[0])
    for r in range(rowLimit):
        for c in range(4):
            W[c][r] = input[step:step + 2]
            step += 2

    return W

# *
#   * toIntMatrix
#   *
#   * Coverts matrix of hex values into a matrix of ints
#   *
#   * @param input: inputted string that is being turned into a matrix
#   * @return: matrix of bytes
def toIntMatrix(input):
    intMatrix = [[0] * 4 for i in range(4)]

    for i in range(4):
        for j in range(4):
            intMatrix[i][j] = int("" + input[i][j], 16)

    return intMatrix

# /*
#    * xor
#    *
#    * This function performs the xor operation on two inputted
#    * hex values.
#    *
#    * Parameters:
#    * s1: the first hex value
#    * s2: the second hex value
#    *
#    * Return value: The hex-value that results from performing the xor
#    * operation.
# */
def xor(s1, s2):
    if (s1 == None):
        s1 = "0"
    
    num1 = int(s1, 16)
    num2 = int(s2, 16)

    result = num1 ^ num2

    hexNum = hex(result)
    hexNum = hexNum[2::].upper()

    if (len(hexNum) == 1):
        hexNum = "0" + hexNum

    return hexNum

# /*
#    * shiftOperation
#    *
#    * The ShiftOperation facilitates AESShiftRow() by performing one shift of to the left.
#    *
#    * Parameters:
#    * matRow: original matrix row.
#    *
#    * Return value: new modified matrix row.
#    * operation.
# */
def shiftOperation(matRow):
    # shift left
    result = [ [0]*4 for i in range(4)]

    result[0] = matRow[3];
    result[1] = matRow[0];
    result[2] = matRow[1];
    result[3] = matRow[2];

    return result


# /*
#    * AESStateXor
#    *
#    * The AESStateXor operation executes xor operation between two matrixes 
#    *
#    * Parameters:
#    * matrix1: first matrix
#    * matrix2: second matrix
#    *
#    * Return value: result of xoring the two matrices.
# */
def AESStateXor(matrix1, matrix2):
    result = [[0] * 4 for i in range(4)]
    for r in range(4):
        for c in range(4):
            result[r][c] = xor(matrix1[r][c], matrix2[r][c])
    return result


# /*
#    * AESNibbleSub
#    *
#    * The AESNibbleSub operation The SubBytes operation replaces each byte in the state matrix
#    * with a corresponding byte from a substitution table called the S-Box.
#    *
#    * Parameters:
#    * inStateHex: state matrix
#    *
#    * Return outStateHex: modified state matrixx
# */
def AESNibbleSub(inStateHex):
    outStateHex = [[0] * 4 for i in range(4)]
    for r in range(4):
        for c in range(4):
            outStateHex[r][c] = aesSBox(inStateHex[r][c])
    return outStateHex

# /*
#    * inverseNibbleSub
#    *
#    * The AESNibbleSub operation The SubBytes operation replaces each byte in the state matrix
#    * with a corresponding byte from a substitution table called the inverse S-Box.
#    *
#    * Parameters:
#    * inStateHex: state matrix
#    *
#    * Return outStateHex: modified state matrixx
# */
def inverseNibbleSub(inStateHex):
    outStateHex = [['0'] * 4 for i in range(4)]
    for r in range(4):
        for c in range(4):
            outStateHex[r][c] = sBoxInverse(inStateHex[r][c])
    return outStateHex


# /*
#    * AESShiftRow
#    *
#    * The AESShiftRow function determines how many times to shift each row of matrix to the left
#    *
#    * Parameters:
#    * inStateHex: state matrix
#    *
#    * Return result: state matrix with rows shifted
# */
def AESShiftRow(inStateHex):
    result = inStateHex

    for r in range(1, 4):
        for i in range(r, 4):
            result[r] = shiftOperation(result[r])

    return result

# /*
#    *
#    * The inverseShiftRow function determines how many times to shift each row of matrix to the right.
#    *
#    * Parameters:
#    * inStateHex: state matrix
#    *
#    * Return result: state matrix with rows shifted to the right
# */
def inverseShiftRow(inStateHex):
    result = inStateHex

    for r in range(1, 4):
        for i in range(r, 4):
            result[r] = inverseShiftOperation(result[r])

    return result
    

# /*
#    *
#    * The AESShiftRow function performs a single shift to the right on a row.
#    *
#    * Parameters:
#    * matRow: single row of matrix
#    *
#    * Return result: right shifted row
# */
def inverseShiftOperation(matRow):
    # shift right
    result = [ [0]*4 for i in range(4)]

    result[0] = matRow[3]
    result[1] = matRow[0]
    result[2] = matRow[1]
    result[3] = matRow[2]

    result[3] = matRow[0]
    result[0] = matRow[1]
    result[1] = matRow[2]
    result[2] = matRow[3]

    return result
  

# /*
#    * AESMixColumn
#    *
#    * This function operates on the columns of the state matrix and applies a linear transformation to
#    * mix the data. We do this by multiplying each column of the state matrix by the fixed matrix
#    * another 
#    *
#    * Parameters:
#    * inStateHex: state matrix
#    *
#    * Return value: adjusted matrix
# */
def AESMixColumn(inStateHex):
    s = toIntMatrix(inStateHex)
    mc = toIntMatrix(mixCols)

    output = [["0"] * 4 for i in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                hexStr = ""

                if mc[j][k] == 1:
                    hexStr = hex(s[k][i])[2:].upper()
                    if len(hexStr) == 1:
                        hexStr = "0" + hexStr
                else:
                    position = inStateHex[k][i]
                    r = position[:1]
                    c = position[1::2]
                    row = int(r, 16)
                    col = int(c, 16)

                    # multiply by 2
                    if mc[j][k] == 2:
                        h = mult2[row][col]
                        hexStr = h[2:].upper()
                    elif mc[j][k] == 3:
                        h = mult3[row][col]
                        hexStr = h[2:].upper()

                ans = xor(output[j][i], hexStr)
                output[j][i] = ans

    return output


# /*
#    * inverseMixColumn
#    *
#    * This function undoes the mixing that was done by AESMixColumns by multiplying columns of the 
#    * state matrix by the fixed inverse matrix. Used in decryption.
#    *  
#    *
#    * Parameters:
#    * inStateHex: state matrix
#    *
#    * Return value: unmixed state matrix
# */
def inverseMixColumn(inStateHex):
    s = toIntMatrix(inStateHex)
    mc = toIntMatrix(invMixCols)
    output = [["0"] * 4 for i in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                hexStr = ""

                if mc[j][k] == 1:
                    hexStr = hex(s[k][i])[2:].upper()
                    if len(hexStr) == 1:
                        hexStr = "0" + hexStr
                else:
                    position = inStateHex[k][i]
                    r = position[:1]
                    c = position[1::2]
                    row = int(r, 16)
                    col = int(c, 16)

                    # multiply by 9
                    if mc[j][k] == 9:
                        h = mult9[row][col]
                        hexStr = h[2:].upper()
                    elif mc[j][k] == 11:
                        h = mult11[row][col]
                        hexStr = h[2:].upper()
                    elif mc[j][k] == 13:
                        h = mult13[row][col]
                        hexStr = h[2:].upper()
                    elif mc[j][k] == 14:
                        h = mult14[row][col]
                        hexStr = h[2:].upper()

                ans = xor(output[j][i], hexStr)
                output[j][i] = ans

    return output



# /*
#    * roundKeysHex
#    *
#    * This function adds the round key to the state matrix during each round of encryption or decryption.
#    * A bitwise XOR operation is performed between the state matrix and round key.
#    *
#    * Parameters:
#    * inStateHex: roundkey
#    *
#    * Return value: adjusted matrix
# */
def roundKeysHex(keyHex):
    W = toByteMatrix(keyHex)
    # insert the input-string values into matrix W in column-major order
    step = 0
    r = 0
    while r < rowLimit:
        for c in range(4):
            W[c][r] = keyHex[step:step + 2]
            step += 2
        r += 1
    
    # j will act as a running column number for matrix W
    j = 4
    # fill the rest of the array
    while j < 44:
        if j % 4 != 0:
            for r in range(rowLimit):
                W[r][j] = xor(W[r][j - 4], W[r][j - 1])
        else:
            # Calculate round
            i = j // 4

            # Shift left
            temp = [[0] * 4 for i in range(4)]
            temp[0] = W[1][j - 1]
            temp[1] = W[2][j - 1]
            temp[2] = W[3][j - 1]
            temp[3] = W[0][j - 1]

            outHex = ""
            for r in range(rowLimit):
                outHex = aesSBox(temp[r])
                temp[r] = outHex

            outHex = aesRcon(i)
            
            temp[0] = xor(outHex, temp[0])

            for r in range(rowLimit):
                W[r][j] = xor(W[r][j - 4], temp[r])
        j += 1

    # Create 11 keys. Each key is a string of 4 columns contents concatenated together.
    roundKeysHex = [0] * 11
    key = 0
    while key < roundKeyLimit - 1:
        output = ""
        col = key * colsPerKey
        while col < key * colsPerKey + colsPerKey:
            for r in range(rowLimit):
                output += W[r][col]
            col += 1
        
        # add output to keyChain
        roundKeysHex[key] = output
        key += 1

    return roundKeysHex


# This function is for if I ever need to print matrix in Terminal. 
def printMatrix(matrix):
    for i in range(rowLimit):
        print("")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
    print("")



# This function drives forward the encryption process by running procedural methods for transforming data
def encrypt(pTextHex, keyHex):
    output = ""
    outputKeys = roundKeysHex(keyHex)
    matrix = toByteMatrix(pTextHex)
    tempKey = AESStateXor(matrix, toByteMatrix(outputKeys[0]))

    roundLimit = 10
    # cycle through rounds
    for r in range(1, 11):
        tempKey = AESNibbleSub(tempKey)
        tempKey = AESShiftRow(tempKey)
        # don't Mix Columns on last round
        if r < roundLimit:
            tempKey = AESMixColumn(tempKey)

        tempKey = AESStateXor(toByteMatrix(outputKeys[r]), tempKey)

    # format key for output
    for i in range(4):
        for j in range(4):
            output += tempKey[j][i]

    return output

# This function drives forward the decryption process by running procedural methods for transforming data
def decrypt(pTextHex, keyHex):
    output = ""
    outputKeys = roundKeysHex(keyHex)
    matrix = toByteMatrix(pTextHex)
    tempKey = AESStateXor(matrix, toByteMatrix(outputKeys[10]))

    roundLimit = 10
    # cycle through rounds
    for r in range(1, 11):
        tempKey = inverseShiftRow(tempKey)
        tempKey = inverseNibbleSub(tempKey)
        tempKey = AESStateXor(toByteMatrix(outputKeys[roundLimit - r]), tempKey)

        # don't Mix Columns on last round
        if r < roundLimit:
            tempKey = inverseMixColumn(tempKey)

    # format key for output
    for i in range(4):
        for j in range(4):
            output += tempKey[j][i]

    return output


tmp = "5468617473206D79204B756E67204675"
roundKeysHex(tmp)

testMatrix1 = [
    ["54", "4F", "4E", "20"],
    ["77", "6E", "69", "54"],
    ["6F", "65", "6E", "77"],
    ["20", "20", "65", "6F"],
]

testMatrix2 = [
    ["54", "73", "20", "67"],
    ["68", "20", "4B", "20"],
    ["61", "6D", "75", "46"],
    ["74", "79", "6E", "75"],
]

testMatrix3 = [
    ["00", "3C", "6E", "47"],
    ["1F", "4E", "22", "74"],
    ["0E", "08", "1B", "31"],
    ["54", "59", "0B", "1A"],
]

testMatrix4 = [
    ["63", "EB", "9F", "A0"],
    ["C0", "2F", "93", "92"],
    ["AB", "30", "AF", "C7"],
    ["20", "CB", "2B", "A2"],
]

testMatrix8 = testMatrix4

testMatrix5 = [
    ["63", "EB", "9F", "A0"],
    ["2F", "93", "92", "C0"],
    ["AF", "C7", "AB", "30"],
    ["A2", "20", "CB", "2B"],
]

testMatrix6 = [
    ["BA", "84", "E8", "1B"],
    ["75", "A4", "8D", "40"],
    ["F4", "8D", "06", "7D"],
    ["7A", "32", "0E", "5D"],
]

result1 = AESStateXor(testMatrix1, testMatrix2) # Tests AESStateXOR
result2 = AESNibbleSub(testMatrix3) # Tests AESNibbleSub
result3 = AESShiftRow(testMatrix4) # Tests ShiftRow
result4 = AESMixColumn(testMatrix5) # Tests MixCols
result5 = inverseMixColumn(testMatrix6) # Tests InverseMixCols
result6 = inverseShiftRow(testMatrix5) # Tests InverseShiftOperation
result7 = inverseNibbleSub(testMatrix8) # Tests InverseNibbleSub