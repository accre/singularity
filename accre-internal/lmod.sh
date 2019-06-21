# -*- shell-script -*-
########################################################################
#  This is the system wide source file for setting up
#  modules:
#
########################################################################

if [ -z "${USER_IS_ROOT:-}" ]; then

  if [ -z "${MODULEPATH_ROOT:-}" ]; then
    export USER=${USER-${LOGNAME}}  # make sure $USER is set
    export LMOD_sys=`uname`

    LMOD_arch=`uname -m`
    if [ "x$LMOD_sys" = xAIX ]; then
      LMOD_arch=rs6k
    fi
    export LMOD_arch

    export MODULEPATH_ROOT="/accre/arch/easybuild/modules/all"
    export LMOD_SETTARG_CMD=":"
    export LMOD_FULL_SETTARG_SUPPORT=no
    export LMOD_COLORIZE=yes
    export LMOD_CASE_INDEPENDENT_SORTING=yes
    export LMOD_PREPEND_BLOCK=normal
    export LMOD_PIN_VERSIONS=yes
    export LMOD_SHORT_TIME=86400
    export MODULEPATH=$(/usr/share/lmod/lmod/libexec/addto --append MODULEPATH $MODULEPATH_ROOT/Core)
    export MODULEPATH=$(/usr/share/lmod/lmod/libexec/addto --append MODULEPATH $MODULEPATH_ROOT/BinDist)
    export MODULESHOME=/usr/share/lmod/lmod
    export LMOD_PACKAGE_PATH=/accre/common/lmod/etc
    export LMOD_AVAIL_STYLE='system:<accre>'
    export LMOD_ADMIN_FILE=/accre/common/lmod/etc/admin.lmod
    export LMOD_RC=/accre/common/lmod/etc/lmodrc.lua

    export BASH_ENV=$MODULESHOME/init/bash

    #
    # If MANPATH is empty, Lmod is adding a trailing ":" so that
    # the system MANPATH will be found
    if [ -z "${MANPATH:-}" ]; then
      export MANPATH=:
    fi
    export MANPATH=$(/usr/share/lmod/lmod/libexec/addto MANPATH /usr/share/lmod/lmod/share/man)
  fi

  PS_CMD=/bin/ps
  if [ ! -x $PS_CMD ]; then
      if   [ -x /bin/ps ]; then
          PS_CMD=/bin/ps
      elif [ -x /usr/bin/ps ]; then
          PS_CMD=/usr/bin/ps
      fi
  fi
  EXPR_CMD=/usr/bin/expr
  if [ ! -x $EXPR_CMD ]; then
      if   [ -x /usr/bin/expr ]; then
          EXPR_CMD=/usr/bin/expr
      elif [ -x /bin/expr ]; then
          EXPR_CMD=/bin/expr
      fi
  fi
  BASENAME_CMD=/bin/basename
  if [ ! -x $BASENAME_CMD ]; then
      if   [ -x /bin/basename ]; then
          BASENAME_CMD=/bin/basename
      elif [ -x /usr/bin/basename ]; then
          BASENAME_CMD=/usr/bin/basename
      fi
  fi


  my_shell=$($PS_CMD -p $$ -ocomm=)
  my_shell=$($EXPR_CMD    "$my_shell" : '-*\(.*\)')
  my_shell=$($BASENAME_CMD $my_shell)
  if [ -f /usr/share/lmod/lmod/init/$my_shell ]; then
     .    /usr/share/lmod/lmod/init/$my_shell >/dev/null # Module Support
  else
     .    /usr/share/lmod/lmod/init/sh        >/dev/null # Module Support
  fi
  unset my_shell PS_CMD EXPR_CMD BASENAME_CMD
fi

# Local Variables:
# mode: shell-script
# indent-tabs-mode: nil
# End:
