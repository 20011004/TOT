# README - Onionscan

Welcome to Onionscan Maltego Transform. You might be wondering what all these files are about. Before you can use the power of
`canari create-profile` you needed to create a transform package and that's exactly what you did here! I've given you a
directory structure to use in the following manner:

* `src/Onionscan` directory is where all your stuff goes in terms of auxiliary modules that you may need for
  your modules
* `src/Onionscan/transforms` directory is where all your transform modules should be placed
* `src/Onionscan/transforms/common` directory is where you can put some common code for your transforms like
  result parsing, entities, etc.
* `src/Onionscan/transforms/common/entities.py` is where you define your custom entities. Take a look at the
  examples provided if you want to play around with custom entities.
* `maltego/` is where you can store your Maltego entity exports.
* `src/Onionscan/resources/maltego` directory is where your `entities.mtz` and `*.machine` files can be
  stored for auto install and uninstall.
* `src/Onionscan/resources/external` directory is where you can place non-Python transforms written in other
  languages.

If you're going to add a new transform in the transforms directory, remember to update the `__all__` variable in
`src/Onionscan/transforms/__init__.py`. Otherwise, `canari install-package` won't attempt to install the
transform. Alternatively, `canari create-transform <transform name>` can be used within the
`src/Onionscan/transforms` directory to generate a transform module and have it automatically added to the
`__init__.py` file, like so:

```bash
$ canari create-transform foo
```

To test your transform, simply `cd` into the src directory and run `canari debug-transform`, like so:

```bash
$ canari debug-transform Onionscan.transforms.onionscan.onionService http://hiddenService.onion
`- MaltegoTransformResponseMessage:  
  `- UIMessages:  
  `- Entities:  
    `- Entity:  {'Type': 'maltego.Phrase'}
      `- Value: hiddenService.onion
      `- Weight: 1
```

Cool right? If you have any further questions don't hesitate to drop me a line;)

Have fun!
