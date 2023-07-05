from src.etl_report import Etl_report


def main():
    etl_report = Etl_report()
    etl_report.run_etl()

if __name__ == '__main__':
    main()