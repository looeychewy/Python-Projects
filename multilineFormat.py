# Justin Liu, 2/12/26
# Program that turns any multiline input into a single-line string, each element separated by commas
# My specific use case, used with https://www.randomlists.com/phone-numbers?qty=20 to quickly input 20 phone numbers into a Wwebsite that accepted multiple inputs so long as separated by commas
# Turn the Bee Movie script from GitHub into an easy copy paste 👍

# Multiline input of phone numbers? -> join by commas
# Wb multiline input of text, broken up into sentence fragments (e.g, Bee Movie script)
# Output/write result to a text file ✅

outFile = open("result.txt", "w")

'''
(854) 778-1785
(485) 472-1161
(445) 633-6287
(693) 876-9563
(606) 699-4010
(478) 225-8401
(923) 690-1912
(836) 293-8828
(608) 259-6618
(921) 319-2006
(620) 764-7199
(377) 524-4973
(794) 474-8910
(277) 354-2510
(726) 553-2304
(204) 816-3685
(447) 699-5934
(724) 814-2427
(840) 926-8360
(437) 211-5816
'''


def main():
    userInput = """
        sekiya@verizon.net
        payned@me.com
        dwsauder@yahoo.ca
        helger@msn.com
        benits@icloud.com
        campware@yahoo.ca
        dkeeler@live.com
        meder@optonline.net
        jesse@aol.com
        sfoskett@att.net
        jshirley@sbcglobal.net
        gmcgath@yahoo.ca
        mhanoh@mac.com
        lukka@msn.com
        fviegas@live.com
        nicktrig@me.com
        earmstro@verizon.net
        overbom@icloud.com
        payned@verizon.net
        bbirth@verizon.net
    """

    updatedNums = userInput.strip().split("\n")

    # now join list items into a string separated by inserted commas
    finalList = ",".join(updatedNums)

    # 2/13, overwriting instead of appending input on new line
    # Need multiple with statements? -> How to keep adding on to file plus including date
    with open("result.txt", "a") as f:
        f.write(finalList)


main()
