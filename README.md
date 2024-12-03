# CSIT327 Documentation

## Online Shopping Ecommerce: Online Shop

**Members**
Rainric Randy P. Yu
Bryle Anthony G. Dinapo
Keith yancy A. Rigodon

### Project Resources

[Gantt Chart](https://docs.google.com/spreadsheets/d/1C3PfKx-7sK16_5QgK9Sc5nPQuVvwR1wF/edit?usp=sharing&ouid=111954012838656286849&rtpof=true&sd=true)

[Functional Requirements](https://docs.google.com/document/d/1BPyiIekjZSr-3ZxI3O1co8hnMoSiAlF9UPLC84fAHmI/edit?usp=sharing)


[Figma Prototype](https://www.figma.com/proto/JTNKVPvM3Tbhcq9Ys31q5A/CSIT327---UI%2FUX?node-id=0-1&t=XJqH76OZ3BGsQwSq-1)
 
[Figma Design (Developer Mode)](https://www.figma.com/design/JTNKVPvM3Tbhcq9Ys31q5A/CSIT327---UI%2FUX?node-id=0-1&m=dev&t=XJqH76OZ3BGsQwSq-1)


# [Online Shopping](https://react.dev/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/main/LICENSE) [![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) [![(Runtime) Build and Test](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml/badge.svg)](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml) [![(Compiler) TypeScript](https://github.com/facebook/react/actions/workflows/compiler_typescript.yml/badge.svg?branch=main)](https://github.com/facebook/react/actions/workflows/compiler_typescript.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://legacy.reactjs.org/docs/how-to-contribute.html#your-first-pull-request)

With Online Shopping you can now order the things you like buy. duh

* **Convenience Anytime, Anywhere:** Online shopping allows you to browse and purchase items at any time and from any location, eliminating the need to visit physical stores and accommodating busy schedules.
* **Wider Variety of Choices:** With access to global marketplaces, you can find a broader range of products, styles, and brands, including unique or rare items unavailable locally.
* **Home Delivery and Convenience** Products are delivered directly to your doorstep, saving time and effort, especially for bulky or heavy items.


## Installation/How to run the program
1. Create a new branch:
    ```sh
    git clone https://github.com/Gideon1274/CSIT327.git
    ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. 1st Step. Go the CSIT327's folder
   ```sh
   cd CSIT327
   ```
4. 2st Step. Go to Ecommerce
   ```sh
   cd ecommerce
   ```
3. 3st Step. Start the server
   ```sh
   py manage.py runserver
   ```
   
## How to create a SuperUser/Admin
 ```sh
py manage.py createsuperuser
 ```


## Documentation

You can find the React documentation [on the website](https://react.dev/).

Check out the [Getting Started](https://react.dev/learn) page for a quick overview.

The documentation is divided into several sections:

* [Quick Start](https://react.dev/learn)
* [Tutorial](https://react.dev/learn/tutorial-tic-tac-toe)
* [Thinking in React](https://react.dev/learn/thinking-in-react)
* [Installation](https://react.dev/learn/installation)
* [Describing the UI](https://react.dev/learn/describing-the-ui)
* [Adding Interactivity](https://react.dev/learn/adding-interactivity)
* [Managing State](https://react.dev/learn/managing-state)
* [Advanced Guides](https://react.dev/learn/escape-hatches)
* [API Reference](https://react.dev/reference/react)
* [Where to Get Support](https://react.dev/community)
* [Contributing Guide](https://legacy.reactjs.org/docs/how-to-contribute.html)

You can improve it by sending pull requests to [this repository](https://github.com/reactjs/react.dev).

## Examples

We have several examples [on the website](https://react.dev/). Here is the first one to get you started:

```jsx
import { createRoot } from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById('container'));
root.render(<HelloMessage name="Taylor" />);
```

This example will render "Hello Taylor" into a container on the page.

You'll notice that we used an HTML-like syntax; [we call it JSX](https://react.dev/learn#writing-markup-with-jsx). JSX is not required to use React, but it makes code more readable, and writing it feels like writing HTML.

## Contributing

The main purpose of this repository is to continue evolving React core, making it faster and easier to use. Development of React happens in the open on GitHub, and we are grateful to the community for contributing bugfixes and improvements. Read below to learn how you can take part in improving React.

### [Code of Conduct](https://code.fb.com/codeofconduct)

Facebook has adopted a Code of Conduct that we expect project participants to adhere to. Please read [the full text](https://code.fb.com/codeofconduct) so that you can understand what actions will and will not be tolerated.

### [Contributing Guide](https://legacy.reactjs.org/docs/how-to-contribute.html)

Read our [contributing guide](https://legacy.reactjs.org/docs/how-to-contribute.html) to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to React.

### [Good First Issues](https://github.com/facebook/react/labels/good%20first%20issue)

To help you get your feet wet and get you familiar with our contribution process, we have a list of [good first issues](https://github.com/facebook/react/labels/good%20first%20issue) that contain bugs that have a relatively limited scope. This is a great place to get started.

### License

React is [MIT licensed](./LICENSE).
