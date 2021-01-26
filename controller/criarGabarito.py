from models.gabaritos import Gabarito


class CriarGabarito():
    perguntas1 = ["1: Quanto é 2-2?","2: Quanto é 2-1?","3: Quanto é 10+10?","4: Quanto é 8-2?","5: Quanto é 12-2?",
                  "6: Quanto é 2*2?","7: Quanto é 2*10?","8: Quanto é 20/2?","9: Quanto é 200/2?",
                  "10: Quanto é 5*2?"]
    perguntas2 = ["1: Quanto é 2-2?", "2: Quanto é 2-1?", "3: Quanto é 10+10?", "4: Quanto é 8-2?", "5: Quanto é 12-2?",
                  "6: Quanto é 2*2?", "7: Quanto é 2*10?", "8: Quanto é 20/2?", "9: Quanto é 200/2?",
                  "10: Quanto é 5*2?"]
    respostas1 = ["0","1","20","6","10","4","20","10","100","10"]
    respostas2 = ["0", "1", "20", "6", "10", "4", "20", "10", "100", "10"]

    gabarito1 = Gabarito(respostas1, perguntas1)

    gabarito2 = Gabarito(respostas2, perguntas2)
