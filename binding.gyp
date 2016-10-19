{
  'targets': [
    {
      'target_name': 'sipster',
      'sources': [
        'src/binding.cc',
        'src/SIPSTERAccount.cc',
        'src/SIPSTERCall.cc',
        'src/SIPSTERMedia.cc',
        'src/SIPSTERTransport.cc',
      ],
      'include_dirs': [
        "src",
        "<!(node -e \"require('nan')\")"
      ],
      'conditions': [
        [ 'OS!="win"', {
          'cflags_cc': [
            '<!@(pkg-config --atleast-version=2.4.5 libpjproject)',
            '<!@(pkg-config --cflags libpjproject)',
            '-fexceptions',
            '-Wno-maybe-uninitialized' # This isn't supported on OS X w/ clang
          ],
          'libraries': [
            '<!@(pkg-config --libs libpjproject)',
          ],
        }],
        [ 'OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS': [
              # Wonderfully enough, gyp on OS X ignores cflags, so we have to do this
              # See https://gist.github.com/TooTallNate/1590684 for details
              '<!@(pkg-config --atleast-version=2.4.5 libpjproject)',
              '<!@(pkg-config --cflags libpjproject)',
              '-fexceptions',
              '-frtti'
            ],
          },

          # begin gyp stupidity workaround =====================================
          'ldflags!': [
            '-framework CoreAudio',
          ],
          'libraries!': [
            'CoreServices', 
            'AudioUnit',
            'AudioToolbox',
            'Foundation',
            'AppKit',
            'QTKit',
            'QuartzCore',
            'OpenGL',
            'AVFoundation',
            'CoreGraphics',
            'CoreVideo',
            'CoreMedia'
          ],
          'libraries': [
            'CoreAudio.framework',
            'CoreServices.framework',
            'AudioUnit.framework',
            'AudioToolbox.framework',
            'Foundation.framework',
            'AppKit.framework',
            'QTKit.framework',
            'QuartzCore.framework',
            'OpenGL.framework',
            'AVFoundation.framework',
            'CoreGraphics.framework',
            'CoreVideo.framework',
            'CoreMedia.framework'
          ],
          # end gyp stupidity workaround =======================================

        }],
      ],
    },
  ],
}
