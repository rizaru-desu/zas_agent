from setuptools import setup, find_packages

setup(
    name="zas_agent",
    version="0.1.2",
    author="Vladimir Ulogov",
    author_email="vladimir.ulogov@zabbix.com",
    license="GNU GPLv3",
    description="Zabbix Agent Simulator",
    long_description="Zabbix Agent Simulator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "zas_agent=zas_agent:main"
        ]
    },
    data_files=[
        ('~/.zas', ['etc/network.scenario']),
        ("~/etc", ["etc/zas_scenario.cfg"]),
        ("~/usr/share/zas_agent", ["doc/zas-agent-0.1.1.pdf"]),
        ("~/usr/share/man/man1", ["doc/zas_agent.py.1"])
    ],
    install_requires=[
        "daemonize==2.4.2",
        "numpy==1.22.0",
        "redis>=2.0.0",
        "simplejson>=2.0.9"
    ],
)
