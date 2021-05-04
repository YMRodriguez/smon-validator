from pdfminer.high_level import extract_text


def processReport(file):
    """This function processes a report for a given timeframe."""
    # First extract relevant text from the report
    text = extract_text(file, page_numbers=[0])
    linedText = list(map(lambda y: y.strip(), filter(lambda x: x != '', text.splitlines())))
    return {"timeframe": extractTimeFrame(linedText),
            "name": extractName(linedText),
            "profit": extractProfit(linedText),
            "accountType": accountType(linedText)}


def accountType(text):
    """This function checks the validity of a lined text."""
    # First validate if it contains any demo account hint.
    if any(list(map(lambda x: 'DEMO' in x, text))):
        return "DEMO"
    return "REAL"


def extractTimeFrame(reportText):
    """ This function returns TimeFrame of the report."""
    pivot1 = reportText.index("Informe de actividad")
    pivot2 = reportText.index("Ayuda")
    resultPivot1 = reportText[pivot1 + 1]
    resultPivot2 = reportText[pivot2 - 1]
    if resultPivot1 == resultPivot2:
        return resultPivot1
    else:
        return "Fail"


def extractName(reportText):
    """ This function returns the name of the author of the report."""
    pivot1 = reportText.index("Valor liquidativo")
    pivot2 = reportText.index("Individual")
    resultPivot1 = reportText[pivot1 + 1]
    resultPivot2 = reportText[pivot2 - 2]
    if resultPivot1 == resultPivot2:
        return resultPivot1
    else:
        return "Fail"


def extractProfit(reportText):
    """ This function returns the profit of the report."""
    pivot1 = reportText.index("Cambio")
    pivot2 = reportText.index("Short")
    resultPivot1 = reportText[pivot1 + 1]
    resultPivot2 = reportText[pivot2 - 1]
    if resultPivot1 == resultPivot2:
        return resultPivot1
    else:
        return "Fail"
