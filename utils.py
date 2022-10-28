from req_info import countries,  cause_names


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
        for cause in causes :
            ex = False
            found_name = False
            for x in cause_names :
                if x == cause:
                    # found_name = True
                    yield x 
                    break
                for i in cause_names[x]:
                    if i == cause:
                        # if found_name :
                        yield  i
                        ex = True
                        break
                        # else :
                        #     yield [x, i]
                        #     ex = True
                        #     break
                if ex :
                    break      
            break 

if __name__ =="__main__":
    x = Validator.country("India")
    d = Validator.category(["Animals"])
    print(list(x))
    print(list(d))