import eplus.eplus
import yaml
import argparse


def main(args):
    config = yaml.load(open("config.yaml"))
    runner = eplus.eplus.Eplus(config)
    runner.run(serial=args.serial_number, num_date=args.date_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('serial_number', type=int)
    parser.add_argument('date_number', type=int, help="何日目か0~5")
    args = parser.parse_args()
    main(args)
