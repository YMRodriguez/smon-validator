from pdfminer.high_level import extract_text


def processReport(file):
    """This function processes a report for a given timeframe."""
    # First extract relevant text from the report
    text = extract_text(file, page_numbers=[0])
    linedText = list(map(lambda y: y.strip(), filter(lambda x: x != '', text.splitlines())))
    accType = accountType(linedText)
    return {"timeframe": extractTimeFrame(linedText),
            "name": extractName(linedText, accType),
            "profit": extractProfit(linedText, accType),
            "accountType": accType}


def accountType(text):
    """This function checks the validity of a lined text."""
    # First validate if it contains any demo account hint.
    if any(list(map(lambda x: 'DEMO' in x, text))):
        return "DEMO"
    return "REAL"


def extractTimeFrame(reportText):
    """ This function returns TimeFrame of the report."""
    pivot1, pivot2 = reportText.index("Informe de actividad"), reportText.index("Ayuda")
    resultPivot1, resultPivot2 = reportText[pivot1 + 1], reportText[pivot2 - 1]
    if resultPivot1 == resultPivot2:
        return resultPivot1
    else:
        return "Fail"


def extractName(reportText, accType):
    """ This function returns the name of the author of the report."""
    if accType == "DEMO":
        pivot1, pivot2 = reportText.index("Total"), reportText.index("Individual")
        resultPivot1, resultPivot2 = reportText[pivot1 + 6], reportText[pivot2 - 2]
    else:
        pivot1, pivot2 = reportText.index("Ayuda"), reportText.index("Margen")
        resultPivot1, resultPivot2 = reportText[pivot1 + 1], reportText[pivot2 - 4]
    if resultPivot1 == resultPivot2:
        return resultPivot1
    else:
        return "Fail"


def extractProfit(reportText, accType):
    """ This function returns the profit of the report."""
    if accType == "DEMO":
        pivot1, pivot2 = reportText.index("Cambio"), reportText.index("Short")
        resultPivot1, resultPivot2 = reportText[pivot1 + 1], reportText[pivot2 - 1]
    else:
        pivot1, pivot2 = reportText.index("Cambio"), reportText.index("Valor inicial")
        resultPivot1, resultPivot2 = reportText[pivot1 + 7], reportText[pivot2 - 3]
    if resultPivot1 == resultPivot2:
        return resultPivot1
    else:
        return "Fail"
