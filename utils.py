from req_info import countries, cause_names


class Validator:
    # reason of using yield instead of return beacouse return will terminate the loop inside our spider too
    @staticmethod
    def country(country):
        for x in countries:
            if x == country:
                yield True
                break
        yield False

    @staticmethod
    def category(causes):
        for cause in causes:
            ex = False
            for x in cause_names:
                if x == cause:
                    yield x
                    # break
                for i in cause_names[x]:
                    if i == cause:
                        yield [x, i]
                        ex = True
                        break
                if ex:
                    break
            break


if __name__ == "__main__":
    x = Validator.country("India")
    d = Validator.category(
        [
            "Performing Arts",
            "Veterinary Services",
        ]
    )
    print(list(x))
    print(list(d))
