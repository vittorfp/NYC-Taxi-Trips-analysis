from os import path
import requests
import logging
import click


output_folder = 'data/raw/'


@click.command()
@click.argument('file_url')
def download_file(file_url):
    logger = logging.getLogger(__name__)
    file_name = file_url.split('/')[-1]

    if path.isfile(output_folder + file_name):
        logger.info('File has already been downloaded: {}'.format(file_name))
        return

    try:
        logger.info('Downloading file: {}'.format(file_name))
        response = requests.get(file_url, allow_redirects=True)
        open(output_folder + file_name, 'w').write(response.text)
    except:
        logger.info('Failed to download: {}'.format(file_name))
        return
    finally:
        logger.info('Successfully downloaded file: {}'.format(file_name))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    download_file()
