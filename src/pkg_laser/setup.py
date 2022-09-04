from setuptools import setup

package_name = 'pkg_laser'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='brunofarias',
    maintainer_email='bruno43ist@yahoo.com.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_laser = pkg_laser.node_laser:main',
            'laser = pkg_laser.laser:main',
            'movement = pkg_laser.movement:main'
        ],
    },
)
