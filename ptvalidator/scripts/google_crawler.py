import google
urls = []
a = google.search('maryla rodowicz nie wystąpi w opolu')
for i in range(10):
    urls.append((next(a)))

print(urls)