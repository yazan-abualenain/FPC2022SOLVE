def GetInputs(inputData : list):
    """
    GetInputs function takes a list of inputs and returns the processed data.
    [num of 1st input args, num of 2nd input args, ...]
    [n1,n2,[index of number of lines has been entered before in nth input],num of args in each line]
    [n1,n2,n3,[value nth, items in each line]]
    """
    Data = inputData.copy()
    outputData = []
    for i in Data:
        
        if isinstance(i, int):
            StdIn = input()
            if StdIn == "":
                break
            else:
                try:
                    StdIn = int(StdIn)
                except ValueError:
                    StdIn.strip()
                    if " " in StdIn:
                        innerData = []
                        StdIn = StdIn.split()
                        for j in StdIn:
                            try:
                                j = int(j)
                            except ValueError:
                                j = j.strip()
                            finally:
                                innerData.append(j)
                        StdIn = innerData
                finally:
                    outputData.append(StdIn)
        elif isinstance(i, list):
            for count in range(outputData[i[0]]):
                StdIn = input()
                if i[1] > 1:
                    innerData = []
                    StdIn = StdIn.split()
                    for j in StdIn:
                        try:
                            j = int(j)
                        except ValueError:
                            j = j.strip()
                        finally:
                            innerData.append(j)
                    StdIn = innerData
                    outputData.append(StdIn)
                else:
                    try:
                        StdIn = int(StdIn)
                    except ValueError:
                        StdIn = str(StdIn).strip()
                    finally:
                        outputData.append(StdIn)
    return tuple(outputData)

