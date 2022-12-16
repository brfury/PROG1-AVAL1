class Individual:
    # auxilia quando não for colocado o nome do individuo
    __indiv_n = 1

    def __init__(self, genotype, name=None):
        self.__genotype = self.__validate_genotype(genotype)
        self.__name = self.__validate_name(name, genotype)
        self.__blood_type = self.__validate_blood_type(self.__genotype)
        self.__agglutinogens = self.__validate_agglutinogens(self.__blood_type)
        self.__agglutinins = self.__validate_agglutinins(self.__blood_type)

    def __validate_genotype(self, genotype):
        valid_types = ("AA", "Ai", "BB", "Bi", "AB", "ii")

        if isinstance(genotype, str) and (genotype in valid_types):
            pass

        elif isinstance(genotype, Individual):
            genotype = genotype.__genotype

        else:
            raise TypeError("Invalid genotype")

        return genotype

    def __validate_name(self, name, genotype):
        if isinstance(name, str):
            # caso necessario, implementar verificador de nome igual aos gerados automaticamente
            pass

        elif name is None:
            if isinstance(genotype, Individual):
                name = genotype.__name

            else:
                name = "Indiv" + str(self.__indiv_n)
                Individual.__indiv_n += 1

        else:
            raise TypeError("Invalid name")

        return name

    def __validate_blood_type(self, genotype):
        if genotype[0] == "i":
            blood_type = "O"

        elif genotype[0] == "B":
            blood_type = "B"

        elif genotype[0] == "A":
            if genotype[1] == "B":
                blood_type = "AB"

            else:
                blood_type = "A"

        else:
            raise TypeError("Invalid type blood")

        return blood_type

    def __validate_agglutinogens(self, blood_type):
        if blood_type == "O":
            agglutinogens = "None"

        elif blood_type == "A":
            agglutinogens = "A"

        elif blood_type == "B":
            agglutinogens = "B"

        else:
            agglutinogens = "A and B"

        return agglutinogens

    def __validate_agglutinins(self, blood_type):
        if blood_type == "O":
            agglutinins = "A and B"

        elif blood_type == "A":
            agglutinins = "B"

        elif blood_type == "B":
            agglutinins = "A"

        else:
            agglutinins = "None"

        return agglutinins

    def __validate_indiv(self, indiv):
        if isinstance(indiv, Individual):
            indiv = indiv.__genotype
        else:
            raise TypeError("The parameter must be Individual")

        return indiv

    def offsprings_genotypes(self, indiv):
        indiv1 = self.__genotype
        if isinstance(indiv, Individual):
            indiv2 = self.__validate_indiv(indiv)

        possibilities = set()
        for i in indiv1:
            count = 0
            while count < 2:
                if (i + indiv2[count]) == "iA":
                    possibilities.add("Ai")

                elif (i + indiv2[count]) == "iB":
                    possibilities.add("Bi")

                elif (i + indiv2[count]) == "BA":
                    possibilities.add("AB")

                else:
                    possibilities.add(i + indiv2[count])
                count += 1

        return tuple(possibilities)

    def offsprings_blood_types(self, indiv):
        indiv1 = self.__genotype
        if isinstance(indiv, Individual):
            indiv2 = indiv

        else:
            raise TypeError("The parameter must be Individual")

        possibilities_genotype = self.offsprings_genotypes(indiv2)
        possibilities_type_blood = set()
        for i in possibilities_genotype:
            if i == "AA" or i == "Ai" or i == "iA":
                possibilities_type_blood.add("A")

            elif i == "BB" or i == "Bi" or i == "iB":
                possibilities_type_blood.add("B")

            elif i == "AB" or i == "BA":
                possibilities_type_blood.add("AB")

            else:
                possibilities_type_blood.add("O")

        return tuple(possibilities_type_blood)

    def can_receive(self, indiv):
        if isinstance(indiv, Individual):
            pass

        else:
            raise TypeError("The parameter must be individual")

        if self.__blood_type == "AB":
            answer = True

        elif self.__blood_type == "A":
            if indiv.__blood_type in ("A", "O"):
                answer = True

            else:
                answer = False

        elif self.__blood_type == "B":
            if indiv.__blood_type in ("B", "O"):
                answer = True

            else:
                answer = False

        else:
            if indiv.__blood_type == "O":
                answer = True

            else:
                answer = False

        return answer

    def can_donate(self, indiv):
        if isinstance(indiv, Individual):
            pass

        else:
            raise TypeError("The parameter must be individual")

        if self.__blood_type == "O":
            answer = True

        elif self.__blood_type == "A":
            if indiv.__blood_type in ("A", "AB"):
                answer = True
            else:
                answer = False

        elif self.__blood_type == "B":
            if indiv.__blood_type in ("B", "AB"):
                answer = True
            else:
                answer = False

        else:
            if indiv.__blood_type == "AB":
                answer = True

            else:
                answer = False

        return answer

    name = property(lambda self: self.__name)

    genotype = property(lambda self: self.__genotype)

    blood_type = property(lambda self: self.__blood_type)

    agglutinogens = property(lambda self: self.__agglutinogens)

    agglutinins = property(lambda self: self.__agglutinins)

    def __str__(self):
        return f"Nome:{self.__name}\nTipo Sanguíneo:{self.__blood_type}"

    def __repr__(self):
        return f"Nome:{self.__name}\nTipo Sanguíneo:{self.__blood_type}"
