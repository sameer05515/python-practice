from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


import future_sip_calculation as fsip


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/interest/calc/{amount}/{interest_rate}/{year}")
async def cal_future_amount(amount: float, interest_rate: float, year: int):
    if amount <= 0:
        raise UnicornException("Amount not valid : " + str(amount))
    if interest_rate < -1 or interest_rate > 1:
        raise UnicornException("Interest rate not valid : " + str(interest_rate))
    if year < 0:
        raise UnicornException("Year not valid : " + str(year))
    fa: float = amount
    for x in range(1, year + 1):
        fa = fa * (1 + interest_rate)
        print(fa)
    return {
        "amount": amount,
        "interest_rate": interest_rate,
        "years": year,
        "future_amt": fa
    }


@app.get("/sip/calc/{amount}/{interest_rate}/{year}")
async def cal_future_sip_amount(amount: float, interest_rate: float, year: int):
    if amount <= 0:
        raise UnicornException("Amount not valid : " + str(amount))
    if interest_rate < -1 or interest_rate > 1:
        raise UnicornException("Interest rate not valid : " + str(interest_rate))
    if year < 0:
        raise UnicornException("Year not valid : " + str(year))

    return fsip.cal_future_sip_amount(amount, interest_rate, year)
