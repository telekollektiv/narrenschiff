# narrenschiff

Disclaimer: written with a 2day deadline on sparetime, pls don't judge.

```
[Online]            [Server]
[http       --->    http]           [Schauspieler]
                    [zmq    <---    zmq]
                                    [text to speech
```

## text2speech

```
# assuming the text2speech program processes every line instantly
./client.py tcp://127.0.0.1:5500 | ./text2speech
# assuming it reads until EOF
./client.py tcp://127.0.0.1:5500 | while read -r x; do echo "$x" | ./text2speech; done
```

## docker
```
docker run -it --rm narrenschiff -p 127.0.0.1:5000:5000 -p 5500:5500 -v $(pwd)/persitent:/app/persistent narrenschiff
```
