import uvicorn
from app.root import app

def main() -> None:
    uvicorn.run(app = app, host = '0.0.0.0', port = 80)
    return

if __name__ == '__main__':
    main()