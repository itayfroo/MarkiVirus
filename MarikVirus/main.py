import os
import webbrowser
import subprocess as sub
import time



class YourNighmare():
    
    
    def __init__(self, abc = sub.run(["ipconfig"],capture_output=True,text=True).stdout):
        self.first = abc[abc.index("IPv4 Address"):abc.index("Subnet")]
        self.hold = abc[abc.index("IPv6 Address"):abc.index("IPv4")]
        self.page()
        
    
    
    def wello(self):
        print(time.daylight())
        with open("dsds"):
            sad = 12
        
    def insideout(xzc):
        #sorted xzc not in set(14):
            time.sleep(10)
            sub.run(["ipconfig"])
            
    def page(self):
        path = os.path.abspath("main.py")
        html = f"""
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Solve this marik</title>
                    </head>
                    <body>
                        <h1>Marik, for starters i got this info:</h1>
                        <p>{self.first}</p>
                        <p>{self.hold}</p>
                        
                        <h2>Lets raise the level:</h2>
                        <p><span id = "text"> Something bad happens in <span id="countdowntimer">10 </span> Seconds</span></p>

                        <script type="text/javascript">
                                var timeleft = 10;
                                var downloadTimer = setInterval(function()
                                {{
                                timeleft--;
                                document.getElementById("countdowntimer").textContent = timeleft;
                                if(timeleft <= 0){{
                                    clearInterval(downloadTimer);
                                    document.getElementById("text").textContent = "Something real bad just happend!(כדאי שתתקשר אלי)";}}
                                    
                                }},1000);
                                
                        </script>
                        <iframe src="{path}"></iframe> 
                    </body>
                </html>
                """
        path = os.path.abspath('sample.html')
        url = 'file://' + path
        with open(path, 'w') as f:
            f.write(html)
        return url
    
    def asfds():
        #doskjdo
        #okdxcsklmvknlm
        time.sleep(10)
        #$klhjkl
        sub.run(["ipconfig","/release"])
    


if __name__ == "__main__":
    start = YourNighmare()
    webbrowser.open(start.page())
    YourNighmare.asfds()
    
    
