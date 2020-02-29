from os import system
import logging
import click


output_folder = 'data/raw/'


@click.command()
@click.argument('file_url')
def download_file(file_url):
    logger = logging.getLogger(__name__)
    file_name = file_url.split('/')[-1]

    try:
        logger.info('Downloading file: {}'.format(file_name))
        system('wget {} -O {} -nc'.format(file_url, output_folder + file_name))
        logger.info('Successfully downloaded file: {}'.format(file_name))
    except:
        logger.info('Failed to download: {}'.format(file_name))
        return


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    download_file()
