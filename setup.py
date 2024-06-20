
from setuptools import find_packages, setup

package_name = 'rpi_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuvraj',
    maintainer_email='yuvraj@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'video_publisher=rpi_robot.video_publisher:main',
            'video_subscriber=rpi_robot.video_subscriber:main',
            
        ],
    },
)
