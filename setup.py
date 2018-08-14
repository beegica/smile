#emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
#ex: set sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See the COPYING file distributed along with the smile package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

from distutils.core import setup
import versioneer
commands = versioneer.get_cmdclass().copy()

setup(name='smile',
      version=version=versioneer.get_version(),
      packages=['smile'],
      package_dir={"smile": "smile"},
      package_data={"smile": ["face-smile.png",
                              "test_sound.wav",
                              "test_video.mp4",
                              "crosshairs*"]},
      author=['Per B. Sederberg'],
      maintainer=['Per B. Sederberg'],
      maintainer_email=['psederberg@gmail.com'],
      url=['http://github.com/compmem/smile'],
      cmdclass=commands)
