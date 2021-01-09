import wikipedia

class WikipediaHandler:
    mapping = {
        "01":"January", 
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December",
    }

    def convert_date(self, date):
        split = str(date).split("-")
        month = split[1]
        day = split[2]
        month = self.mapping[month]

        if day[0] == "0": # if 01
            day = day[1]  # day = 1

        return f"{day} {month}"

    def get_summary(self, date):
        query = self.convert_date(date)

        print(f"Fetching the wikipedia entry of {query}")
        summary = wikipedia.summary(query, sentences=30)
        return summary

