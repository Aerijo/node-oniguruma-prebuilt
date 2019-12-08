{
  'targets': [
    {
      'target_name': 'oniguruma',
      'type': 'static_library',
      'conditions': [
        ['OS=="win"', {
          'msvs_disabled_warnings': [
            4244,  # conversion from '__int64' to 'int', possible loss of data
          ],
          'defines': [
            'ONIG_EXTERN=extern',
          ],
        }],
        ['OS=="linux"', {
          'cflags': [
            '-w',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'deps/oniguruma',
          'deps/oniguruma/src'
        ],
      },
      'include_dirs': [
        'deps/oniguruma',
        'deps/oniguruma/src'
      ],
      'sources': [
        'deps/oniguruma/src/oniggnu.h',
        'deps/oniguruma/src/onigposix.h',
        'deps/oniguruma/src/oniguruma.h',
        'deps/oniguruma/src/regcomp.c',
        'deps/oniguruma/src/regenc.c',
        'deps/oniguruma/src/regenc.h',
        'deps/oniguruma/src/regerror.c',
        'deps/oniguruma/src/regexec.c',
        'deps/oniguruma/src/regext.c',
        'deps/oniguruma/src/reggnu.c',
        'deps/oniguruma/src/regint.h',
        'deps/oniguruma/src/regparse.c',
        'deps/oniguruma/src/regparse.h',
        'deps/oniguruma/src/regposerr.c',
        'deps/oniguruma/src/regposix.c',
        'deps/oniguruma/src/regsyntax.c',
        'deps/oniguruma/src/regtrav.c',
        'deps/oniguruma/src/regversion.c',
        'deps/oniguruma/src/st.c',
        'deps/oniguruma/src/st.c',
        'deps/oniguruma/src/ascii.c',
        'deps/oniguruma/src/big5.c',
        'deps/oniguruma/src/cp1251.c',
        'deps/oniguruma/src/euc_jp.c',
        'deps/oniguruma/src/euc_kr.c',
        'deps/oniguruma/src/euc_tw.c',
        'deps/oniguruma/src/gb18030.c',
        'deps/oniguruma/src/iso8859_1.c',
        'deps/oniguruma/src/iso8859_2.c',
        'deps/oniguruma/src/iso8859_3.c',
        'deps/oniguruma/src/iso8859_4.c',
        'deps/oniguruma/src/iso8859_5.c',
        'deps/oniguruma/src/iso8859_6.c',
        'deps/oniguruma/src/iso8859_7.c',
        'deps/oniguruma/src/iso8859_8.c',
        'deps/oniguruma/src/iso8859_9.c',
        'deps/oniguruma/src/iso8859_10.c',
        'deps/oniguruma/src/iso8859_11.c',
        'deps/oniguruma/src/iso8859_13.c',
        'deps/oniguruma/src/iso8859_14.c',
        'deps/oniguruma/src/iso8859_15.c',
        'deps/oniguruma/src/iso8859_16.c',
        'deps/oniguruma/src/koi8.c',
        'deps/oniguruma/src/koi8_r.c',
        'deps/oniguruma/src/mktable.c',
        'deps/oniguruma/src/sjis.c',
        'deps/oniguruma/src/unicode.c',
        'deps/oniguruma/src/utf16_be.c',
        'deps/oniguruma/src/utf16_le.c',
        'deps/oniguruma/src/utf32_be.c',
        'deps/oniguruma/src/utf32_le.c',
        'deps/oniguruma/src/utf8.c',
      ],
    },
    {
      'target_name': 'onig_scanner',
      'dependencies': [
        'oniguruma'
      ],
      'include_dirs': [ '<!(node -e "require(\'nan\')")' ],
      'sources': [
        'src/onig-result.cc',
        'src/onig-reg-exp.cc',
        'src/onig-scanner.cc',
        'src/onig-scanner-worker.cc',
        'src/onig-searcher.cc',
        'src/onig-string.cc'
      ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': ['-std=c++11', '-stdlib=libc++'],
            'MACOSX_DEPLOYMENT_TARGET': '10.7.0',
          }
        }],
        ['OS in "linux solaris"', {
          'cflags': [
            '-std=c++0x',
            '-Wno-unused-result',
            '-Wno-missing-field-initializers',
          ],
          'cflags_cc!': [
            '-fno-rtti'
          ]
        }],
        ['OS=="win"', {
          'msvs_disabled_warnings': [
            4244,  # conversion from 'double' to 'int', possible loss of data
            4267,  # conversion from 'size_t' to 'int', possible loss of data
            4530,  # C++ exception handler used, but unwind semantics are not enabled
          ],
          'msvs_settings': {
            'VCCLCompilerTool' : {
              'AdditionalOptions' : ['/EHsc']
            }
          },
          'defines': [
            'ONIG_EXTERN=extern',
          ],

        }],
        ['OS=="freebsd"', {
          'cflags': [
            '-std=c++0x',
          ]
        }]
      ]
    }
  ]
}
