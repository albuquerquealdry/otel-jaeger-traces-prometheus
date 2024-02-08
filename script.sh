TIMES=1000
for i in $(eval echo "{1..$TIMES}")
do
    siege -c 1 -r 10 http://localhost:8000/bulbasaur
    siege -c 3 -r 5 http://localhost:8000/pikachu
    siege -c 2 -r 10 http://localhost:8000/random_status/mewtwo
    siege -c 1 -r 1 http://localhost:8000/random_sleep/ditto
    siege -c 1 -r 1 http://localhost:8000/error_test/meowth
    sleep 5
done